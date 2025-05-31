from fastmcp import FastMCP
from movie_recommender.crew import MovieRecommender
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
    inputs = {
        'query': input,
        'current_date': str(datetime.now().date)
    }

    try:
        result = MovieRecommender().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    return result
