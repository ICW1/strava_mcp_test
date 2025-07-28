import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

from mistralai import Mistral
from mistralai.extra.run.context import RunContext
from mistralai.extra.mcp.stdio import MCPClientSTDIO, StdioServerParameters

# Configuration
MODEL = "mistral-medium-latest"
ENV = {
    "STRAVA_CLIENT_ID": os.environ.get("STRAVA_CLIENT_ID"),
    "STRAVA_CLIENT_SECRET": os.environ.get("STRAVA_CLIENT_SECRET"), 
    "STRAVA_REFRESH_TOKEN": os.environ.get("STRAVA_REFRESH_TOKEN")
}

async def query_strava_async(user_query):
    """Query Strava via MCP"""
    api_key = os.environ["MISTRAL_API_KEY"]
    client = Mistral(api_key)
    
    server_params = StdioServerParameters(
        command="python",
        args=["/Users/iancrowe-wright/repos/strava-mcp-server/src/strava_server.py"],
        env=ENV,
    )
    mcp_client = MCPClientSTDIO(stdio_params=server_params)

    async with RunContext(model=MODEL) as run_ctx:
        await run_ctx.register_mcp_client(mcp_client=mcp_client)
        
        run_result = await client.beta.conversations.run_async(
            run_ctx=run_ctx,
            inputs=user_query,
        )
        
        return run_result.output_as_text


def query_strava(user_query):
    """Synchronous wrapper"""
    try:
        return asyncio.run(query_strava_async(user_query))
    except Exception as e:
        return f"Error: {str(e)}"