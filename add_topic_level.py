import pandas as pd
import constants

TOPIC = constants.topic
GRADE = constants.grade
SUBJECT = constants.subject
GENERATOR = "Quiz Wizard"

# Load your excel file into a pandas DataFrame
df = pd.read_excel("~/Downloads/excel.xlsx")

# Create new columns
df.insert(0, "Topic", TOPIC)
df.insert(1, "Grade", GRADE)
df.insert(2, "Subject", SUBJECT)
df.insert(3, "Generator", GENERATOR)

# Write the DataFrame back to the Excel file
df.to_excel("~/Downloads/excel.xlsx", index=False)
