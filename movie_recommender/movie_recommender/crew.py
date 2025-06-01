from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from crewai_tools import SerperDevTool
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource
from movie_recommender.tools.movie_api_tool import MovieApiTool
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

serper_dev_tool = SerperDevTool()
json_source = JSONKnowledgeSource(
    file_paths=["test_movies.json",
                "recent_test_movies.json"]
)

movie_tool = MovieApiTool()


@CrewBase
class MovieRecommender():
    """MovieRecommender crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst'],
            verbose=True
        )

    @agent
    def consultant(self) -> Agent:
        return Agent(
            config=self.agents_config['consultant'],
            verbose=True,
            # knowledge_sources=[json_source]
            tools=[movie_tool]
        )

    @agent
    def searcher(self) -> Agent:
        return Agent(
            config=self.agents_config['searcher'],
            verbose=True,
            tools=[serper_dev_tool]
        )

    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'],
            verbose=True,
        )

    @task
    def analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyst_task'],
        )

    @task
    def consultant_task(self) -> Task:
        return Task(
            config=self.tasks_config['consultant_task'],

        )

    @task
    def searcher_task(self) -> Task:
        return Task(
            config=self.tasks_config['searcher_task'],
            # human_input=True
        )

    @task
    def summarizer_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarizer_task'],
            output_file='io/output.txt'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MovieRecommender crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
            # knowledge_sources=[json_source]
        )
