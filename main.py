import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain_community.llms import Ollama

load_dotenv()

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

search_tool = SerperDevTool()

llm = Ollama(model='openhermes')

researcher = Agent(
    llm=llm,
    role="Senior Financial Analyst",
    goal="Identify financially sound investment opportunities.",
    backstory="You are an experienced financial analyst specializing in real estate investments. Your task is to identify financially promising real estate opportunities in Mumbai.",
    allow_delegation=False,
    tools=[search_tool]
)

task1 = Task(
    description="Conduct research to find 5 financially promising real estate investment suburbs in Mumbai, India. Provide key financial metrics such as average property prices, rental yields, price-to-rent ratios, and any economic indicators relevant to investment decisions.",
    expected_output="""A detailed financial report of each suburb. The results should be formatted like this:
    
    Suburb Name: Mumbai
    Mean Property Price: $1 million
    Rental Yield: 3.5%
    Price-to-Rent Ratio: 28.57
    Economic Indicators:
    - GDP Growth: 7.5%
    - Unemployment Rate: 4.2%
    Background Information: These suburbs are typically located near major transport hubs, employment centers, and educational institutions. The following list highlights some of the top contenders for investment opportunities.""",
    agent=researcher,
    output_file="task1_output.txt"
)

writer = Agent(
    llm=llm,
    role="Investment Advisor",
    goal="Provide actionable investment advice based on financial data.",
    backstory="You are an investment advisor specializing in real estate. Your task is to distill the financial information provided by the analyst into actionable advice for potential investors.",
    allow_delegation=False,
    verbose=True,
)

task2 = Task(
    description="Create a concise investment recommendation report based on the financial data provided.",
    expected_output="A concise investment recommendation report outlining the top investment opportunities in Mumbai, along with reasons for their financial viability and potential risks.",
    agent=writer,
    output_file="task2_output.txt",
)

crew = Crew(agents=[researcher, writer], tasks=[task1, task2], verbose=2)

task_output = crew.kickoff()
print(task_output)
