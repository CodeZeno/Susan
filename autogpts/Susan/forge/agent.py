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
        Need to get Susan to create a plan with steps and the ability she will need for each (Max 1 ability per step)
        
        """

        # Get this step's task from the database
        task = await self.db.get_task(task_id)

        # Create a new step in the database
        step = await self.db.create_step(
            task_id=task_id, input=step_request, is_last=True
        )

        # Log the message
        #LOG.info(f"\t✅ Final Step completed: {step.step_id} input: {step.input[:19]}")

        # Initialise the prompt engine
        prompt_engine = PromptEngine("gpt-3.5-turbo")

        # Load a prompt from a file
        system_prompt = prompt_engine.load_prompt("system-format")

        # Initialize the messages list with the system prompt
        messages = [
            {"role": "system", "content": system_prompt},
        ]

        # Define the task parameters
        task_kwargs = {
            "task": task.input,
            "abilities": self.abilities.list_abilities_for_prompt(),
        }

        #LOG.info("List of abilities: %s", task_kwargs["abilities"])

        # Load the task prompt with the defined task parameters
        task_prompt = prompt_engine.load_prompt("task-step", **task_kwargs)

        # Append the task prompt to the messages list
        messages.append({"role": "user", "content": task_prompt})

        try:
            # Define the parameters for the chat completion request
            chat_completion_kwargs = {
                "messages": messages,
                "model": "gpt-3.5-turbo",
            }
            # Make the chat completion request and parse the response
            chat_response = await chat_completion_request(**chat_completion_kwargs)
            answer = json.loads(chat_response["choices"][0]["message"]["content"])

            # Log the answer for debugging purposes
            LOG.info(pprint.pformat(answer))

        except json.JSONDecodeError as e:
            # Handle JSON decoding errors
            LOG.error(f"Unable to decode chat response: {chat_response}")
        except Exception as e:
            # Handle other exceptions
            LOG.error(f"Unable to generate chat response: {e}")

        # Verify that ability is valid and run it
        if "ability" in answer:
            ability = answer["ability"]
            if ability["name"] in self.abilities.abilities:
                LOG.info(f"Running ability: { ability['name'] }")
                try:
                    # todo: store step output? create the next step?
                    step.output = await self.abilities.run_ability(
                        task_id, ability['name'], **ability["args"]
                    )
                    LOG.info(f"output: { step.output }")
                except Exception as e:
                    LOG.error(f"Unable to run ability({ ability['name'] }): {e}")
            else:
                LOG.error(f"Unknown ability: { ability['name'] }")

        if not step.output:
            # Set the step output to the "speak" part of the answer
            step.output = answer["thoughts"]["speak"]

        # Return the completed step
        return step
