from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from research_assistant.types import ProjectPlan

@CrewBase
class ResearchAssistantGenerativeAI():
    """ResearchAssistantGenerativeAI: Contains research on the benefits of adopting LangGraph as an agent framework"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def analyst_task_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst_task_creator'],
            verbose=True
        )

    @agent
    def interviewing_analyst_1(self) -> Agent:
        return Agent(
            config=self.agents_config['interviewing_analyst_1'],
            verbose=True
        )

    @agent
    def interviewing_analyst_2(self) -> Agent:
        return Agent(
            config=self.agents_config['interviewing_analyst_2'],
            verbose=True
        )
    
    @agent
    def interviewing_analyst_3(self) -> Agent:
        return Agent(
            config=self.agents_config['interviewing_analyst_3'],
            verbose=True
        )

    @agent
    def ai_expert_interviewed_1(self) -> Agent:
        return Agent(
            config=self.agents_config['ai_expert_interviewed_1'],
            verbose=True
        )
    
    @agent
    def ai_expert_interviewed_2(self) -> Agent:
        return Agent(
            config=self.agents_config['ai_expert_interviewed_2'],
            verbose=True
        )

    @agent
    def ai_expert_interviewed_3(self) -> Agent:
        return Agent(
            config=self.agents_config['ai_expert_interviewed_3'],
            verbose=True
        )

    @agent
    def expert_technical_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['expert_technical_writer'],
            verbose=True
        )    

    @task
    def subtask_creator_for_analyst(self) -> Task:
        return Task(
            config=self.tasks_config['subtask_creator_for_analyst'],
            agent=self.analyst_task_creator()
        )

    @task
    def task_interview_analyst_1(self) -> Task:
        return Task(
            config=self.tasks_config['task_interview_analyst_1'],
            agent=self.interviewing_analyst_1()
        )

    @task
    def task_interview_analyst_2(self) -> Task:
        return Task(
            config=self.tasks_config['task_interview_analyst_2'],
            agent=self.interviewing_analyst_2()
        )
    
    @task
    def task_interview_analyst_3(self) -> Task:
        return Task(
            config=self.tasks_config['task_interview_analyst_3'],
            agent=self.interviewing_analyst_3()
        )

    @task
    def task_ia_specialist_1(self) -> Task:
        return Task(
            config=self.tasks_config['task_ia_specialist_1'],
            agent=self.ai_expert_interviewed_1()
        )

    @task
    def task_ia_specialist_2(self) -> Task:
        return Task(
            config=self.tasks_config['task_ia_specialist_2'],
            agent=self.ai_expert_interviewed_2()
    )

    @task
    def task_ia_specialist_3(self) -> Task:
        return Task(
            config=self.tasks_config['task_ia_specialist_3'],
            agent=self.ai_expert_interviewed_3()
        )

    @task
    def task_expert_technical_writer(self) -> Task:
        return Task(
            config=self.tasks_config['task_expert_technical_writer'],
            agent=self.expert_technical_writer(),
        )

    @crew
    def crew(self) -> Crew:
        """creates a report on the benefits of adopting LangGraph as an agent framework"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,  # Sequential execution: breakdown → estimate → allocate
            verbose=True
        )
