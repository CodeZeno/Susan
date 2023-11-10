from ..registry import ability

@ability(
  name="step2",
  description="Enters sms code to pass security check when logging into email address",
  parameters=[
      {
          "name": "code",
          "description": "The 4 digit sms code sent to the user",
          "type": "string",
          "required": True,
      }
  ],
  output_type="string",
)
async def step2(agent, task_id: str, code: str) -> str:
  return f"I used {code} to login and you have 32 unread emails."