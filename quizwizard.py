from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os
import random
import constants
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

level = constants.level
grade = constants.grade
subject = constants.subject
topic = constants.topic
number_of_questions = constants.number_of_questions

driver_path = "/opt/homebrew/bin/chromedriver"

options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--profile-directory=Default')
options.add_argument("--incognito")
options.add_argument("--disable-plugins-discovery")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

url = "https://app.getquizwizard.com/create-content/context"

driver.get(url)
delay = random.uniform(0.2, 1)

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

# SOURCE PAGE
source_button = driver.find_element(
    "class name", "InputButton_color-blue__BD8sN")
source_button.click()

topic_field = driver.find_element("name", "sourceTopic")
topic_field.send_keys(topic)

time.sleep(delay)

subject_field = driver.find_element("name", "sourceField")
subject_field.send_keys(subject)

time.sleep(delay)

level_field = driver.find_element("name", "sourceSector")
level_field = Select(level_field)
level_field.select_by_value(level)

time.sleep(delay)

class_field = driver.find_element("name", "sourceLevel")
class_field.send_keys(grade)

time.sleep(delay)

continue_button = driver.find_element("class name", "Button_container__31fZ8")
continue_button.click()

time.sleep(1)

# CONTENT PAGE
type_buttons = driver.find_elements(
    "class name", "InputButton_container__l5ahQ")
content_button = type_buttons[0]
content_button.click()
time.sleep(delay)
all_buttons = driver.find_elements(
    "class name", "InputButton_container__l5ahQ")
answers_type_button = all_buttons[2]
answers_type_button.click()

number_correct = driver.find_element("name", "questionsAnswerMCQnTrue")
# number_correct.send_keys("1")
number_wrong = driver.find_element("name", "questionsAnswerMCQnFalse")
# number_wrong.send_keys("3")
time.sleep(delay)

# number_of_questions_field = driver.find_element("name", "n")
# number_of_questions_field.send_keys(
#     Keys.COMMAND + "a")  # or Keys.COMMAND + "a" on Mac
# number_of_questions_field.send_keys(Keys.DELETE)
# number_of_questions_field.send_keys(number_of_questions)

generate_question_button = driver.find_element(
    "class name", "Button_content__JvV2b")
generate_question_button.click()

# STATEMENT OF QUESTIONS
# answers_type = driver.find_element("class name", "AnswerType_mcq__td3pY")
# driver.execute_script("arguments[0].scrollIntoView();", answers_type)
# answers_type.click()
#
# time.sleep(delay)

# Use WebDriverWait to wait up to 10 seconds for the element to appear
wait = WebDriverWait(driver, 39)

# Wait until an element with the specified class name is present

element = wait.until(EC.presence_of_element_located(
    ("class name", "QuestionsMCQ_question-container__sN1YD")))

container = driver.find_element(
    "class name", "Footer_footer-inner__-hlY0")
children = container.find_elements("xpath", ".//*")

export_button = children[0]

export_button.click()

time.sleep(delay)

# EXPORT PAGE
excel_button = driver.find_element("class name", "ExportModal_excel__2i68v")
excel_button.click()

time.sleep(0.9)

driver.quit()
