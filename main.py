from selenium import webdriver
import time

def load_cookies_from_file(filename):
    cookie_list = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(':')
            if len(parts) == 2:
                cookie_list.append((parts[0], parts[1]))
    return cookie_list

loaded_cookie_list = load_cookies_from_file('cookies.txt')

driver = webdriver.Firefox()

driver.get('https://ticket.melon.com/csoon/detail.htm?csoonId=7635')

for cookie_name, cookie_value in loaded_cookie_list:
    driver.add_cookie({"name": cookie_name, "value": cookie_value})

driver.refresh()

time.sleep(10)

driver.quit()
