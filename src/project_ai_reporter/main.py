#!/usr/bin/env python
# src/project_ai_reporter/main.py
import sys
from project_ai_reporter.crew import CoachingAndWritingCrew

def run():
    """
    Run the crew with user input for topic and selected skills.
    """
    # Get the topic and skills from user input
    topic = input("Enter the topic you want to discuss: ")
    skills = input("Enter the skills ('active_listening, empathy'): ").split(',')

    # Prepare inputs for the crew
    inputs = {
        'topic': topic.strip(),
        'skills': [skill.strip() for skill in skills]
    }

    # Kick off the process
    CoachingAndWritingCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
