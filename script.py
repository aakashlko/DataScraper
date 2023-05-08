import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as cdm
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


with open('companies.txt', 'r') as companies_file:
    companies = [line.strip() for line in companies_file]


def main(info):
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(service=Service(
        executable_path=cdm().install()), options=chrome_options)

    driver.get("https://www.wikipedia.org/")

    time.sleep(1)

    driver.find_element(
        By.XPATH, '/html/body/div[3]/form/fieldset/div/input').send_keys(info)

    time.sleep(1)

    driver.find_element(
        By.XPATH, '/html/body/div[3]/form/fieldset/button').click()

    time.sleep(2)

    main = driver.find_element(
        By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[2]')

    return main.text

    time.sleep(2)


with open('data.txt', 'a') as data_file:
    for company in companies:
        main_data = main(company)
        data_file.writelines(company + ":" + main_data + "\n \n")
