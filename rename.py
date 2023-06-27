import os

old_file = os.path.expanduser("~/Downloads/excel.xlsx")
new_file = os.path.expanduser("~/Downloads/generated_question.xlsx")

os.rename(old_file, new_file)
