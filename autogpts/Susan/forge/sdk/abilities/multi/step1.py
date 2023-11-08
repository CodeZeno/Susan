from ..registry import ability

@ability(
  name="step1",
  description="Turns a word into it's plural form.",
  parameters=[
      {
          "name": "word",
          "description": "The word that needs to be converted to it's plural form.",
          "type": "string",
          "required": True,
      }
  ],
  output_type="string",
)
async def step1(agent, task_id: str, word: str) -> str:
  return word + "s"