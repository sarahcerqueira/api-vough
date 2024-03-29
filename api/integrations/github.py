import os
import requests
import json


class GithubApi:
    API_URL = os.environ.get("GITHUB_API_URL", "https://api.github.com")
    #GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "3171f52300b31637b69828731e680c848b6eb7ee")
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "5c305526a1b9a2430a0aacd9fac483d6e1db13bd")

    def __init__(self):
        self.autenticacao = {'Authorization': 'token' + self.GITHUB_TOKEN}


    def get_organization(self, login:str):
        """Busca uma organização no Github

        :login: login da organização no Github
        """

        session = requests.Session()
        result = session.get(self.API_URL + '/orgs/'+ login, headers=self.autenticacao)

        if result.status_code == 404:
            return None

        elif result.status_code >= 400 and result.status_code <= 499:
            return 403

        return  json.loads(result.text)

    def get_organization_public_members(self, login: str) -> int:
        """Retorna todos os membros públicos de uma organizaçãoexit

        :login: login da organização no Github
        """
        session = requests.Session()
        result = session.get(self.API_URL + '/orgs/'+ login +'/public_members', headers=self.autenticacao)

        if result.status_code == 404:
            return None

        elif result.status_code >= 400 and result.status_code <= 499:
            return 403

        orgs = json.loads(result.text)
        length = len(orgs)

        return length



    