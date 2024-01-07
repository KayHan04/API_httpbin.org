import pytest

from API import Testclass
from settings import auth, random_codes, random_value

tc = Testclass()


# HTTP metods tests
@pytest.mark.skip
def test_delete_method():
    status, resault = tc.delete_metod()
    assert status == 200
    assert resault == {
        "args": {},
        "data": "",
        "files": {},
        "form": {},
        "headers": {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru,en-US;q=0.9,en;q=0.8",
            "Cookie": "stale_after=never; fake=fake_value; last_nonce=d6be22d6b600de06e81f3f860dd450bd",
            "Host": "httpbin.org",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "X-Amzn-Trace-Id": "Root=1-6599815a-595a16a240274ca23e61b48e"
        },
        "json": 'null',
        "origin": "95.104.199.219",
        "url": "https://httpbin.org/delete"
    }


@pytest.mark.skip
def test_get_metod():
    status, resault = tc.get_metods()
    assert status == 200
    assert resault == {
        "args": {},
        "headers": {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru,en-US;q=0.9,en;q=0.8",
            "Cookie": "stale_after=never; fake=fake_value; last_nonce=d6be22d6b600de06e81f3f860dd450bd",
            "Host": "httpbin.org",
            "Referer": "https://httpbin.org/",
            "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "X-Amzn-Trace-Id": "Root=1-65993a52-0bb8e8a96c1161ff4cb24adb"
        },
        "origin": "95.104.199.219",
        "url": "https://httpbin.org/get"
    }


@pytest.mark.skip
def test_patch_metod():
    status, resault = tc.patch_metod()
    assert status == 200
    assert resault == {
        "args": {},
        "data": "",
        "files": {},
        "form": {},
        "headers": {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru,en-US;q=0.9,en;q=0.8",
            "Cookie": "stale_after=never; fake=fake_value; last_nonce=d6be22d6b600de06e81f3f860dd450bd",
            "Host": "httpbin.org",
            "Origin": "https://httpbin.org",
            "Referer": "https://httpbin.org/",
            "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "X-Amzn-Trace-Id": "Root=1-6599820c-579a04420afea43b2d12b3b2"
        },
        "json": 'null',
        "origin": "95.104.199.219",
        "url": "https://httpbin.org/patch"
    }


@pytest.mark.skip
def test_post_metod():
    status, resault = tc.post_metod()
    assert status == 200
    assert resault == {
        "args": {},
        "data": "",
        "files": {},
        "form": {},
        "headers": {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru,en-US;q=0.9,en;q=0.8",
            "Content-Length": "0",
            "Cookie": "stale_after=never; fake=fake_value; last_nonce=efcf91377144d53d58c8680678ce61e7",
            "Host": "httpbin.org",
            "Origin": "https://httpbin.org",
            "Referer": "https://httpbin.org/",
            "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "X-Amzn-Trace-Id": "Root=1-6599bd0b-334d2e9473ab194c57685ad0"
        },
        "json": 'null',
        "origin": "95.104.199.219",
        "url": "https://httpbin.org/post"
    }


@pytest.mark.skip
def test_put_metod():
    status, resault = tc.put_metod()
    assert status == 200
    assert resault == {
        "args": {},
        "data": "",
        "files": {},
        "form": {},
        "headers": {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru,en-US;q=0.9,en;q=0.8",
            "Content-Length": "0",
            "Cookie": "stale_after=never; fake=fake_value; last_nonce=efcf91377144d53d58c8680678ce61e7",
            "Host": "httpbin.org",
            "Origin": "https://httpbin.org",
            "Referer": "https://httpbin.org/",
            "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "X-Amzn-Trace-Id": "Root=1-6599bd3e-147215e66266e86f7e57d657"
        },
        "json": 'null',
        "origin": "95.104.199.219",
        "url": "https://httpbin.org/put"
    }


# -------------------------------------------------------------------------------
# Auth metods
@pytest.mark.xfail
def test_get_api():
    status, resault = tc.get_api(user='Andrei', passwd='04123')
    assert status == 200


@pytest.mark.xfail
def test_bearer():
    status, resault = tc.get_bearer(auth)
    assert status == 200


@pytest.mark.xfail
def test_auth_gigest():
    status, resault = tc.get_digest_auth(qop="passcode123", user='Andrei', passwd='04123')
    assert status == 200


@pytest.mark.xfail
def test_auth_gigest_algO():
    status, resault = tc.get_digest_algorithm(qop="passcode123", user='Andrei', passwd='04123', algagithm='MD5')
    assert status == 200


# --------------------------------------------------------------------------------
# Status codes
def test_status_random_status_code():
    status, resault = tc.delete_status(codes=random_codes)
    if status == 100:
        print('Informational responses')
    elif status == 200:
        print('Success')
    elif status == 300:
        print('Redirection')
    elif status == 400:
        print('Client Errors')
    else:
        status == 500
        print('Server Errors')
    assert status == 200


# ----------------------------------------------------------------------------------
# Request inspection

def test_header():
    status, resault = tc.get_header()
    assert status == 200
    print(resault)


def test_ip():
    status, resault = tc.get_ip()
    assert status == 200
    assert resault == {
        "origin": "95.104.199.219"
    }


def test_user_agent():
    status, resault = tc.get_user_agent()
    assert status == 200
    assert resault == {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }


# --------------------------------------------------------------------------------------
# Response inspection

def test_cache():
    status, resault = tc.cache()
    assert status == 200


def test_cache_value():
    status, resault = tc.cache_value(value=random_value)
    assert status == 200


def test_etag():
    status, resault = tc.etag()
    assert status == 200


def test_response_headers():
    status, resault = tc.response_headers()
    assert status == 200


def test_response_headers_post():
    status, resault = tc.post_response_headers()
    assert status == 200


# -----------------------------------------------------------------------------------
# Cookies
def test_cookie():
    status, resault = tc.cookie()
    assert status == 200
    assert resault == {
        "cookies": {
            "fake": "fake_value",
            "last_nonce": "d6be22d6b600de06e81f3f860dd450bd",
            "stale_after": "never"
        }
    }
