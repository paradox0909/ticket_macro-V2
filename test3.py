from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Firefox Start 
driver = webdriver.Firefox()

# 웹 페이지 열기
driver.get('https://ticket.melon.com/performance/index.htm?prodId=209371')


for cookie_name, cookie_value in cookie_list:
    driver.add_cookie({"name": cookie_name, "value": cookie_value})

wait = WebDriverWait(driver, 30)  # 최대 20초간 대기

#첫번째 버튼
xpath = '//*[@id="dateSelect_20240303"]/button'
wait.until(EC.presence_of_element_located((By.XPATH, xpath))).click()
#두번째 버튼
xpath_second_button = '//*[@id="ticketReservation_Btn"]'
wait.until(EC.presence_of_element_located((By.XPATH, xpath_second_button))).click()

