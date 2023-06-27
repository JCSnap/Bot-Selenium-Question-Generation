import os
from flask import Flask, request, jsonify
import openai
import constants
import requests
import json
import time
import re

openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL = "gpt-4"

number_of_questions = constants.number_of_questions
grade = constants.grade

QUESTION_SPLIT_INSTRUCTION = constants.prompt_check_instruction(
    constants.number_of_questions, constants.grade)

SETTINGS = """
Language: English
Student educational level: {grade} 
Number of questions: 1
Question type(s): MCQ
"""

# QUESTION SPLIT
completion = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": QUESTION_SPLIT_INSTRUCTION},
        {"role": "user", "content": constants.topic}
    ]
)

subtopics = completion.choices[0].message.content

lines = subtopics.split("\n")
print(lines)

subtopics = [re.sub(r'^\d+\. ', '', line)
             for line in lines if re.match(r'^\d+\. ', line)]

prompt = SETTINGS + "\n"

for i in range(1):
    prompt = SETTINGS + "\n" + subtopics[i] + constants.MCQ_FORMAT + "\n"
    completion = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": constants.QUESTION_GENERATION_INSTRUCTION},
            {"role": "user", "content": prompt}
        ]
    )
    question = completion.choices[0].message.content
    print(question)

    # Split the text by double newlines to get each section separately
    sections = question.split("\n\n")

    # Parse the question
    question = sections[1].replace("Question: ", "")

    # Parse the options
    options_text = sections[2].replace("Options:\n", "")
    options = re.findall(r'\. (.*)', options_text)

    # Parse the answer
    answer_text = sections[3].replace("Answer: ", "")
    answer = ord(answer_text) - ord('A')  # convert from letter to index

    print("Question:", question)
    print("Options:", options)
    print("Answer:", answer)
