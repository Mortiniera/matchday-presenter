import asyncio
import os
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

async def get_tools_async():
    """Connects to the mcp-reddit server via uvx and returns the tools and exit stack."""
    print("--- Attempting to start and connect to mcp-reddit MCP server via uvx ---")
    try:
        # Check if uvx is available
        await asyncio.create_subprocess_shell('uvx --version', stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

        # Check if the MCP server is running
        tools, exit_stack = await MCPToolset.from_server(
            connection_params=StdioServerParameters(
                command='uvx',
                args=['--from', 'git+https://github.com/adhikasp/mcp-reddit.git', 'mcp-reddit'],
                env={'REDDIT_CLIENT_ID': os.getenv('REDDIT_CLIENT_ID'),
                     'REDDIT_CLIENT_SECRET': os.getenv('REDDIT_CLIENT_SECRET'),
                     'REDDIT_USER_AGENT': os.getenv('REDDIT_USER_AGENT')}
            )
        )

        # Print discovered tool names for debugging/instruction refinement
        print(f"--- Successfully connected to mcp-reddit server. Discovered {len(tools)} tool(s). ---")
        
        for tool in tools:
            print(f"  - Discovered tool: {tool.name}")
        return tools, exit_stack
    except FileNotFoundError:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!! ERROR: 'uvx' command not found. Please install uvx: pip install uvx !!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # Return empty tools and a no-op exit stack to prevent agent failure
        class DummyExitStack:
            async def __aenter__(self): return self
            async def __aexit__(self, *args): pass
        return [], DummyExitStack()
    except Exception as e:
        print(f"--- ERROR connecting to or starting mcp-reddit server: {e} ---")
        # This prevents the agent from failing
        class DummyExitStack:
            async def __aenter__(self): return self
            async def __aexit__(self, *args): pass
        return [], DummyExitStack()

async def create_agent():
    """ creates the agent instance after fetching tools from the MCP server."""
    tools, exit_stack = await get_tools_async()
    discovered_tool_name = "fetch_reddit_hot_threads"
    if not tools:
        print("--- Warning: No tools discovered from MCP server. Agent will lack Reddit functionality. ---")
    
    agent_instance = Agent(
        name="reddit_agent",
        description="A Reddit agent that searches for hot posts in a given subreddit using an external MCP Reddit tool.",
        tools=tools,
        model="gemini-1.5-flash-latest",
        instruction=(
            "You are the Async Reddit News Agent. Your task is to fetch hot post titles from any subreddit using the connected Reddit MCP tool."
            "1. **Identify Subreddit:** Determine which subreddit the user wants news from. Use 'championsleague' by default if none are specified. Use the specific subreddit(s) if mentioned (e.g., 'psg', 'ArsenalFC')."
            f"2. **Call Discovered Tool:** You **MUST** look for and call the tool named '{discovered_tool_name}' with the identified subreddit name and optionally a limit."
            "3. **Present Results:** The tool will return a formatted string containing the hot post information or an error message."
            "   - Present this string directly to the user."
            "   - Clearly state which subreddit the information is from."
            "   - If the tool returns an error message, relay that message accurately."
            "4. **Handle Missing Tool:** If you cannot find the required Reddit tool, inform the user that you cannot fetch Reddit news due to a configuration issue."
            "5. **Do Not Hallucinate:** Only provide information returned by the tool."
        ),
    )

    return agent_instance, exit_stack


root_agent = create_agent()