import json

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


class Testclass:

    def __init__(self):
        self.base_url = 'https://httpbin.org'

    # HTTP metods
    def delete_metod(self) -> json:

        res = requests.delete(self.base_url + '/delete')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def get_metod(self) -> json:

        res = requests.get(self.base_url + '/get')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def patch_metod(self) -> json:

        res = requests.patch(self.base_url + '/patch')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def post_metod(self) -> json:

        res = requests.post(self.base_url + '/post')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def put_metod(self) -> json:

        res = requests.put(self.base_url + '/put')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    # -------------------------------------------------------------------
    #  Auth metods
    def get_api(self, user, passwd) -> json:
        headers = {"Accept": 'application/json',
                   "authority": 'httpbin.org',
                   }
        res = requests.get(self.base_url + '/basic-auth' + f'/{user}' + f'/{passwd}', headers=headers)
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def get_bearer(self) -> json:

        res = requests.get(self.base_url + '/bearer')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def get_digest_auth(self, qop: str, user: str, passwd: str) -> json:

        res = requests.get(self.base_url + '/digest-auth' + f'/{qop}' + f'/{user}/' + f'/{passwd}')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def get_digest_algorithm(self, qop: str, user: str, passwd: str, algorithm: str) -> json:

        res = requests.get(self.base_url + '/digest-auth/' + f'{qop}' + f'{user}/' + f'{passwd}/' + f'{algorithm}')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    # -------------------------------------------------------------------------------------
    # Status code

    def delete_status(self, codes: str) -> json:
        res = requests.delete(self.base_url + '/status/' + f'{codes}')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    # --------------------------------------------------------------------------
    # Request inspection
    def get_header(self) -> json:

        res = requests.get(self.base_url + '/headers')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def get_ip(self) -> json:

        res = requests.get(self.base_url + '/ip')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def get_user_agent(self) -> json:

        res = requests.get(self.base_url + '/user-agent')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    # -------------------------------------------------------------------------------------
    # Response inspection

    def cache(self) -> json:

        headers = {"If-Modified-Since": '1',
                   "If-None-Match": '2',
                   }
        res = requests.get(self.base_url + '/cache', headers=headers)
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def cache_value(self, value) -> json:

        res = requests.get(self.base_url + '/cache' + f'/{value}')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def etag(self) -> json:
        headers = {"If-None-Match": '1',
                   "If-Match": '2',
                   }
        res = requests.get(self.base_url + '/etag' + '/{etag}', headers=headers)
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def response_headers(self) -> json:
        _filter = {"freeform": 'Biba'
                   }
        res = requests.get(self.base_url + '/response-headers', params=_filter)
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def post_response_headers(self) -> json:
        filter = {"freeform": 'Boba'
                  }
        res = requests.post(self.base_url + '/response-headers', params=filter)
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    # -----------------------------------------------------------------------------------
    # Cookies
    def cookie(self) -> json:
        res = requests.get(self.base_url + '/cookies')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault
