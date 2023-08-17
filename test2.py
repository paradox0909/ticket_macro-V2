from selenium import webdriver
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
loaded_cookie_list = load_cookies_from_file('cookies.txt')

# Firefox 브라우저 시작
driver = webdriver.Firefox()

# 웹 페이지 열기
driver.get('https://ticket.melon.com/csoon/detail.htm?csoonId=7635')

# 불러온 쿠키 정보를 적용
for cookie_name, cookie_value in loaded_cookie_list:
    driver.add_cookie({"name": cookie_name, "value": cookie_value})

# 페이지 새로고침
driver.refresh()

# 웹사이트 로딩이 완료될 때까지 대기 (10초)
time.sleep(10)

# 브라우저 닫기
driver.quit()
