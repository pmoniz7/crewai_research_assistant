#!/usr/bin/env python
from dotenv import load_dotenv
load_dotenv()

import sys
import warnings
from datetime import datetime
from pathlib import Path
from pprint import pprint

import pandas as pd
import nbformat
from nbformat.v4 import new_notebook, new_code_cell

from research_assistant.crew import ResearchAssistantGenerativeAI

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

##topic = """The benefits of adopting CrewAI  as an agent framework"""
topic = input("Digite o seu tópico a ser persquisado pelos Agentes de IA: ")
print(topic)

# Input dictionary for the crew
inputs = {
    'topic': topic
}

def run():
    """
    Run the content planning crew, display results, and export a notebook.
    """
    try:
        crew_instance = ResearchAssistantGenerativeAI().crew()
        result = crew_instance.kickoff(inputs=inputs)

        # Token usage reporting
        crew_instance.calculate_usage_metrics()
        usage = crew_instance.usage_metrics

        if usage:
            cost_per_token = 0.150 / 1_000_000  # Adjust for your model
            total_tokens = usage.prompt_tokens + usage.completion_tokens
            total_cost = total_tokens * cost_per_token

            print("\n--- 📊 Usage Summary ---")
            print(f"Prompt tokens: {usage.prompt_tokens}")
            print(f"Completion tokens: {usage.completion_tokens}")
            print(f"Total tokens: {total_tokens}")
            print(f"Estimated total cost: ${total_cost:.4f}")
        else:
            print("Usage metrics not available.")

        ####PRM
        # Try to extract final output from known CrewAI formats
        final_output = None
        if hasattr(result, "final_output"):
            final_output = result.final_output
        elif hasattr(result, "output"):
            final_output = result.output
        elif isinstance(result, str):
            final_output = result
        else:
            final_output = str(result)

        if final_output:
            print("\n=== Research Assistant Report ===\n")
            print(final_output)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
            filename = f"Research_Assistant_Report_{timestamp}.md"
            Path("outputs").mkdir(parents=True, exist_ok=True)
            with open(f"outputs/{filename}", "w", encoding="utf-8") as f:
                f.write(final_output)

            print(f"\nReport saved to outputs/{filename}")
        else:
            print("No output content returned.")

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        ResearchAssistantGenerativeAI().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ResearchAssistantGenerativeAI().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution with mock inputs.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    try:
        ResearchAssistantGenerativeAI().crew().test(
            n_iterations=int(sys.argv[1]),
            openai_model_name=sys.argv[2],
            inputs=inputs            
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()
