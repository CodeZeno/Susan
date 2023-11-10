from ..registry import ability
import requests

@ability(
  name="fetch_url",
  description="Retrieves the contents of a URL",
  parameters=[
      {
          "name": "url",
          "description": "Target URL to fetch",
          "type": "string",
          "required": True,
      }
  ],
  output_type="string",
)
async def fetch_url(agent, task_id: str, url: str) -> str:
  response = requests.get(url)
  return response.text