from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Firefox Start 
driver = webdriver.Firefox()

# 웹 페이지 열기
driver.get('https://ticket.melon.com/performance/index.htm?prodId=209371')

cookie_list = [
    ("JSESSIONID", "E75BAF7B0EA0BABD8CEB2FBC00B3048F"),
    ("KAUTH", "M182RzNqcndCdC1uYXZjNGJGN1Rmelo4ZDFUQ0wwby1mX05UaVZYOUNqMTAyd0FBQVlwZnl1bWklM0J6OUNVM2hTMTdEN0NoSlVzdFBRRGc3aDdyOUtnUG1BYVVteGxZSWhnQ2oxMDJ3QUFBWXBmeXVtaCUzQiUzQiUzQiUzQiUzQg=="),
    ("keyCookie", "49285145"),
    ("MAC", "uehtloThD/AvpxsuVPsVqM8FYsiKEDe9Uxb/af9h1GQyvIAZZi3oaDYvduUgxM/B"),
    ("MLCP", "NDkyODUxNDUlM0IlMjNrYWthb19rbWcwNDExeTY4eDZqJTNCJTNCMCUzQmV5SmhiR2NpT2lKSVV6STFOaUo5LmV5SnBjM01pT2lKdFpXMWlaWEl1YldWc2IyNHVZMjl0SWl3aWMzVmlJam9pYldWc2IyNHRhbmQwSWl3aWFXRjBJam94Tmprek9ESTBNalE0TENKdFpXMWlaWEpMWlhraU9pSTBPVEk0TlRFME5TSXNJbUYxZEc5TWIyZHBibGxPSWpvaVRpSjkuOXZLVkxqWEJkVDRYUVZVSldFaWQybG1pTGdIbks4UXhvYXRfQlBRTnJxayUzQiUzQjA5MDQxOTQ0MDglM0IlRUIlQUQlOTglRUIlQTElOUMlRUQlOTUlQTAlRUElQjklOEMlM0IxJTNCa21nMDQxMXklNDBuYXZlci5jb20lM0IzJTNC"),
    ("MUS", "-1520254322"),
    ("PC_PCID", "16976242047191950443296"),
    ("PCID", "16976242047191950443296"),
    ("TKT_POC_ID", "MP15"),
    ("wcs_bt", "s_585b06516861:1706184927"),
    ("NA_SAC", "dT1odHRwcyUzQSUyRiUyRnRpY2tldC5tZWxvbi5jb20lMkZyZXNlcnZhdGlvbiUyRnBvcHVwJTJGc3RlcEZpbmlzaC5odG0lM0Zyc3J2U2VxJTNEMjAyNDAxMjUwNDE3OTc5MCUyNmNoa0FncmVlQ2hhbm5lbCUzRHxyPWh0dHBzJTNBJTJGJTJGdGlja2V0Lm1lbG9uLmNvbSUyRnJlc2VydmF0aW9uJTJGcG9wdXAlMkZzdGVwRGVsdnkuaHRtJTNGcHJvZElkJTNEMjA5MzcxJTI2c2NoZWR1bGVObyUzRDEwMDAwNCUyNmZpcnN0U2VhdElkJTNENzM4XzE0NyUyNnBlcmZTdGFydERheSUzRDIwMjQwMzEwJTI2aW50ZXJsb2NrVHlwZUNvZGUlM0Q="),
    ("NetFunnel_ID", "WP15"),
]

for cookie_name, cookie_value in cookie_list:
    driver.add_cookie({"name": cookie_name, "value": cookie_value})

wait = WebDriverWait(driver, 30)  # 최대 20초간 대기

#첫번째 버튼
xpath = '//*[@id="dateSelect_20240303"]/button'
wait.until(EC.presence_of_element_located((By.XPATH, xpath))).click()
#두번째 버튼
xpath_second_button = '//*[@id="ticketReservation_Btn"]'
wait.until(EC.presence_of_element_located((By.XPATH, xpath_second_button))).click()

