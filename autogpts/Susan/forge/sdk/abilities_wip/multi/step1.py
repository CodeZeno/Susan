from ..registry import ability
import json

@ability(
  name="step1",
  description="Attempts to log into the users email",
  parameters=[
      {
          "name": "email",
          "description": "Email address to log into",
          "type": "string",
          "required": True,
      }
  ],
  output_type="string",
)
async def step1(agent, task_id: str, email: str) -> str:
  result = {
    "email_address": email,
    "unread": "32"
  }
  return json.dumps(result)
"""
@ability(
  name="step1",
  description="Attempts to log into the users email",
  parameters={
      {
          "type": "object"
          "properties": {
              "email": {
                  "type": "string",
                  "description": "Email address to log into"
              }
          }
          "required": ["email"],
      }
  }
)
"""