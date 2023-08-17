from selenium import webdriver
import time
# Firefox Start 
driver = webdriver.Firefox()

# 웹 페이지 열기
driver.get('https://ticket.melon.com/csoon/detail.htm?csoonId=7635')

# [SET COOKIES MY_SESSION_COOKIE AND KEYS]
cookie_list = [
    ("JSESSIONID", "4A5B9AA94440CE5611F0383E69B21C3D"),
    ("KAUTH", "Mnh6UUJSSTF2SHJFTkFiOGt1aWVWSWp2QWZOcDFIQUEyWl9waWt4dUNpb2xEUUFBQVluLVpnbzUlM0J0V29oX3FpMlY4dzVtemFuTE5FT0NkUXU2Q09hTkxMR0M5OGExa0J5Q2lvbERRQUFBWW4tWmdvMyUzQiUzQiUzQiUzQiUzQg=="),
    ("keyCookie", "48188821"),
    ("MAC", "pg2RI8UD2J/q3f6qm0Rp/Gf027vi887dGlh4EGtFWNIgP/PfiDCW2hXz2SzwzFYe5iRK1LhKatqJ9YsXPDPSnw=="),
    ("MLCP", "NDgxODg4MjElM0IlMjNrYWthb19kb2tpbmdrbnMwOTA5cGRjdSUzQiUzQjAlM0JleUpoYkdjaU9pSklVekkxTmlKOS5leUpwYzNNaU9pSnRaVzFpWlhJdWJXVnNiMjR1WTI5dElpd2ljM1ZpSWpvaWJXVnNiMjR0YW5kMElpd2lhV0YwSWpveE5qa3lNVGt3TWpRM0xDSnRaVzFpWlhKTFpYa2lPaUkwT0RFNE9EZ3lNU0lzSW1GMWRHOU1iMmRwYmxsT0lqb2lUaUo5Ll9XVWRoVTJkajc4U2ZXbXEyelpQdVZIY2diZUJteGtoc0Q5ZXRVQlVQeTAlM0IlM0IwODE2MjE1MDQ3JTNCUGFyYWRveExpeiUzQjElM0Jkb2tpbmdrbnMwOTA5JTQwbmF2ZXIuY29tJTNCMyUzQg=="),
    ("MUS", "1149506888"),
    ("PC_PCID", "16921902083967808656161"),
    ("PCID", "16921902083967808656161"),
    ("TKT_POC_ID", "MP15"),
    ("wcs_bt", "s_585b06516861:1692190266")
]

for cookie_name, cookie_value in cookie_list:
    driver.add_cookie({"name": cookie_name, "value": cookie_value})

driver.refresh()

driver.implicitly_wait(10)

time.sleep(10)

driver.quit()
