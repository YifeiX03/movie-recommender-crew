from fastmcp import FastMCP
from movie_recommender.main import run_input
from datetime import datetime


mcp = FastMCP("Demo")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.resource("greetings://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


@mcp.tool()
def call_crew(input: str) -> str:
    # print(input)
    result = run_input(input)
    return result.raw
