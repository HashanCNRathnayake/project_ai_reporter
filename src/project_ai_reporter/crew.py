# src/project_ai_reporter/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
# llm=ChatOpenAI(
#     model="ollama/llama3.2:1b",
#     api_key="NA",
#     base_url="http://localhost:11434/v1"
#     # base_url="http://localhost:11434/v1"
# )

@CrewBase
class CoachingAndWritingCrew():
    """Coaching and Writing Crew"""

    @agent
    def coach(self) -> Agent:
        return Agent(
            config=self.agents_config['coach'],
            verbose=True,
            tools=[SerperDevTool()]
            # llm=llm
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],
            verbose=True
        )

    @task
    def coaching_task(self) -> Task:
        return Task(
            config=self.tasks_config['coaching_task'],
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'],
            output_file='output/{topic}_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Coaching and Writing Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
