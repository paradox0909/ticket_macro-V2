function getAllCookies() {
    var cookies = document.cookie.split('; ');
    var cookieObject = {};

    for (var i = 0; i < cookies.length; i++) {
        var parts = cookies[i].split('=');
        var key = parts[0];
        var value = parts[1];
        cookieObject[key] = value;
    }

    return cookieObject;
}

// 쿠키 객체를 문자열로 변환하여 출력 ** 중요함.
function displayCookiesAsString() {
    var cookies = getAllCookies();
    var result = '';

    for (var key in cookies) {
        result += key + ': ' + cookies[key] + '\n';
    }

    console.log(result);
}

// 함수 호출
displayCookiesAsString();
