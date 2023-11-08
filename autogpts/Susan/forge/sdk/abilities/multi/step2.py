from ..registry import ability

@ability(
  name="step2",
  description="Add user friendly text explaining that their word is now in it's plural form.",
  parameters=[
      {
          "name": "word",
          "description": "The word that was made into it's plural form",
          "type": "string",
          "required": True,
      }
  ],
  output_type="string",
)
async def step2(agent, task_id: str, word: str) -> str:
  return f"The plural form of your word is: {word}"