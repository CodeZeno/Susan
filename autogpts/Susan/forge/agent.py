from forge.sdk import (
    Agent,
    AgentDB,
    ForgeLogger,
    Step,
    StepRequestBody,
    Task,
    TaskRequestBody,
    Workspace,
    PromptEngine,
    chat_completion_request,
    ChromaMemStore,
)
from .sdk import PromptEngine
import json
import pprint

LOG = ForgeLogger(__name__)

class ForgeAgent(Agent):
    def __init__(self, database: AgentDB, workspace: Workspace):
        """
        The database is used to store tasks, steps and artifact metadata. The workspace is used to
        store artifacts. The workspace is a directory on the file system.

        Feel free to create subclasses of the database and workspace to implement your own storage
        """
        super().__init__(database, workspace)
        self.llm_model = "gpt-3.5-turbo-1106";
        self.prompt_engine = PromptEngine(self.llm_model)

    async def create_task(self, task_request: TaskRequestBody) -> Task:
        """
        The agent protocol, which is the core of the Forge, works by creating a task and then
        executing steps for that task. This method is called when the agent is asked to create
        a task.

        We are hooking into function to add a custom log message. Though you can do anything you
        want here.
        """
        task = await super().create_task(task_request)
        LOG.info(
            f"📦 Task created: {task.task_id} input: {task.input[:40]}{'...' if len(task.input) > 40 else ''}"
        )
        return task

    async def execute_step(self, task_id: str, step_request: StepRequestBody) -> Step:
        """
        #Testing code
        test_req = {
            "model": "gpt-3.5-turbo-1106",
            "response_format": { "type": "json_object" },
            "messages": [
                {
                    "role": "system",
                    "content": "Ensure your reply is valid JSON with these parameters:\n'response' - Your response to the user.\n'plan' - An optional array of steps with each step having a 'name' and 'description'. Use the 'plan' parameter if the request requires multiple steps or tasks to complete the goal.\nYou may alternatively use any of the tools available if you feel they are needed."
                },
                {
                    "role": "user",
                    "content": "Answer as an expert in Planning. \nYour task is:\n\nWhat is the capital of Australia?\n\nAnswer in the provided format.\n\nYour decisions must always be made independently without seeking user assistance. Play to your strengths as an LLM and pursue simple strategies.\n"
                }
            ],
            "tools": [
                {
                    "type": "function",
                    "function": {
                        "name": "get_pizza",
                        "description": "Get the users favorite pizza",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "pizza": {
                                    "type": "string",
                                    "description": "The name of their favorite pizza."
                                }
                            },
                            "required": ["pizza"]
                        }
                    }
                }
            ],
            "tool_choice": "none"
        }
        step = await self.db.create_step(
            task_id=task_id,
            input=step_request,
            is_last=True
        )
        test = await chat_completion_request(**test_req)
        print(json.dumps(test, indent=4))
        step.output = test
        return step
        """
        print("starting...:")
        task = await self.db.get_task(task_id)
        
        new_messages = []
        old_messages = await self.db.get_chat_history(task_id)
        print("old_messages:", json.dumps(old_messages, indent=2))

        last_step = True

        if not old_messages: # First run
            system_prompt = self.prompt_engine.load_prompt("system")
            user_prompt = self.prompt_engine.load_prompt("plan", task=task.input)
            new_messages.append({"role": "system", "content": system_prompt})
            new_messages.append({"role": "user", "content": user_prompt})
            last_step = False
        elif step_request.input:
            new_messages.append({ "role":"user", "content":step_request.input })

        step = await self.db.create_step(
            task_id=task_id,
            input=step_request,
            is_last=last_step
        )
        
        llm_request = {
            "model": self.llm_model,
            "response_format": { "type": "json_object" },
            "messages": old_messages + new_messages,
            "tools": self.abilities.list_abilities_for_tools(),
            "tool_choice": "auto"
        }
        print("LLM Request:", json.dumps(llm_request, indent=2))

        try:
            llm_response = await chat_completion_request(**llm_request)
            answer = llm_response["choices"][0]["message"]
            new_messages.append(answer)
            print("LLM Answer:", json.dumps(answer, indent=2))
        except Exception as e:
            LOG.error(f"Unable to communicate with {self.prompt_engine}: {e}")
            raise
        
        plan = []
        if tools := answer.get("tool_calls"):
            for tool in tools:
                ability = tool["function"]
                try:
                    ability_result = await self.abilities.run_ability(
                        task_id, ability["name"], **json.loads(ability["arguments"])
                    )
                    new_messages.append(
                        {
                            "role": "tool",
                            "tool_call_id": tool["id"],
                            "content": ability_result
                        }
                    )
                except Exception as e:
                    LOG.info(f"Problem running ability { ability['name'] }: { e }")

            llm_request_with_answers = {
                "model": self.llm_model,
                "response_format": { "type": "json_object" },
                "messages": old_messages + new_messages
            }
            print("LLM Final Request:", json.dumps(llm_request_with_answers, indent=2))
            llm_response_final = await chat_completion_request(**llm_request_with_answers)
            answer = llm_response_final["choices"][0]["message"]
            new_messages.append(answer)
            print("LLM Final Response:", json.dumps(answer, indent=2))

        if output := json.loads(answer.get("content")):
            if plan := output.get("plan"):
                LOG.info(f"Houston we have a plan { plan }")
                #step.output = plan + response
                #modify output with plan steps
            else:
                step.output = output.get("response")
        else:
            step.output = answer["content"]

        # filter out tool_calls as they have no content
        filtered_messages = [msg for msg in new_messages if not (msg.get("role") == "assistant" and "tool_calls" in msg)]
        # filter out tool as they must match a tool_call
        filtered_messages = [msg for msg in filtered_messages if msg.get("role") != "tool"]

        # Save filtered messages to DB, this will have all we need for history
        await self.db.add_chat_history(task_id=task_id, messages=filtered_messages)

        step = await self.db.update_step(
            task_id=task_id,
            step_id=step.step_id,
            status="completed",
            output=step.output
        )

        # Return the completed step
        return step