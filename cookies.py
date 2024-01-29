def save_cookie_to_file(cookie_str, file_path):
    with open(file_path, 'w') as file:
        file.write(cookie_str)

# 예시 쿠키 값 (수정 필요)
cookie_value = "keyCookie=testvalue; otherCookie=othervalue;"

# 파일 경로 지정 (수정 필요)
file_path = '/Users/paradoxmyung/Desktop/Paradox/Ive_macro/test.txt'

# 쿠키 값을 파일에 저장
save_cookie_to_file(cookie_value, file_path)

print(f"쿠키가 {file_path}에 저장되었습니다.")
