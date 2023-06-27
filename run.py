from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os
import random

############
# SETTINGS #
############
level = "high"  # low, middle, high
grade = "12th grade"
subject = "Physics"
topic = "Superposition"
number_of_questions = "5"

driver_path = "/opt/homebrew/bin/chromedriver"
driver = webdriver.Chrome()

url = "https://app.getquizwizard.com/create-content/context"

driver.get(url)
delay = random.uniform(1, 2)

time.sleep(delay)

# First export password in terminal, export PASSWORD="password"
# Retrieve the password from the environment variable
password = os.getenv('PASSWORD')

# LOGIN PAGE
email_field = driver.find_element("id", "email")
email_field.send_keys("justinwoody1234@gmail.com")

password_field = driver.find_element("id", "password")
password_field.send_keys(password)

time.sleep(delay)

submit_button = driver.find_element("class name", "Button_container__31fZ8")
submit_button.click()

time.sleep(3)

# TOPIC PAGE
subject_field = driver.find_element("name", "field")
subject_field.send_keys(subject)

time.sleep(delay)

level_field = driver.find_element("name", "sector")
level_field = Select(level_field)
level_field.select_by_value(level)

time.sleep(delay)

class_field = driver.find_element("name", "level")
class_field.send_keys(grade)

time.sleep(delay)

topic_field = driver.find_element("name", "topic")
topic_field.send_keys(topic)

time.sleep(delay)

submit_button = driver.find_element("class name", "Button_container__31fZ8")
submit_button.click()

time.sleep(2)

# CONTENT PAGE
content_button = driver.find_element(
    "class name", "QuestionType_container__tRcUr")
content_button.click()

time.sleep(delay)

number_of_questions_field = driver.find_element("name", "n")
number_of_questions_field.send_keys(
    Keys.COMMAND + "a")  # or Keys.COMMAND + "a" on Mac
number_of_questions_field.send_keys(Keys.DELETE)
number_of_questions_field.send_keys(number_of_questions)

generate_question_button = driver.find_element(
    "class name", "Button_container__31fZ8")
generate_question_button.click()

time.sleep(5)

# STATEMENT OF QUESTIONS
answers_type = driver.find_element("class name", "AnswerType_mcq__td3pY")
driver.execute_script("arguments[0].scrollIntoView();", answers_type)
answers_type.click()

time.sleep(delay)

number_correct = driver.find_element("name", "answersMCQTrue")
# number_correct.send_keys("1")
number_wrong = driver.find_element("name", "answersMCQFalse")
# number_wrong.send_keys("3")

all_buttons = driver.find_elements("class name", "Button_container__31fZ8")
generate_answers_button = all_buttons[1]
generate_answers_button.click()

time.sleep(15)
container = driver.find_element(
    "class name", "AnswersMCQGenerate_footer__TAkKh")
children = container.find_elements("xpath", ".//*")

export_button = children[0]

export_button.click()

time.sleep(delay)

# EXPORT PAGE
excel_button = driver.find_element("class name", "ExportModal_excel__2i68v")
excel_button.click()

time.sleep(delay)

driver.quit()
