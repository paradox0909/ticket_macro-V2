from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 세션 쿠키 정보를 텍스트 파일로부터 불러오기
def load_cookies_from_file(filename):
    cookie_list = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(':')
            if len(parts) == 2:
                cookie_list.append((parts[0], parts[1]))
    return cookie_list

# 텍스트 파일로부터 쿠키 정보 불러오기
loaded_cookie_list = load_cookies_from_file('mingun.txt')

# Firefox 브라우저 시작
driver = webdriver.Firefox()

# 웹 페이지 열기
driver.get('https://ticket.melon.com/performance/index.htm?prodId=209371')

# 불러온 쿠키 정보를 적용
for cookie_name, cookie_value in loaded_cookie_list:
    driver.add_cookie({"name": cookie_name, "value": cookie_value})

# 대기 설정
wait = WebDriverWait(driver, 20)  # 최대 20초간 대기

#첫번째 버튼
xpath = '//*[@id="dateSelect_20240303"]/button'
wait.until(EC.presence_of_element_located((By.XPATH, xpath))).click()
#두번째 버튼
xpath_second_button = '//*[@id="ticketReservation_Btn"]'
wait.until(EC.presence_of_element_located((By.XPATH, xpath_second_button))).click()