#from django.test import TestCase
from api.integrations.github import GithubApi
import unittest


# Create your tests here.

class GithubApiTest(unittest.TestCase):

    def test_get_organization(self):
        githubapi = GithubApi()
        p1 = githubapi.get_organization('collectiveidea')
        self.assetEquals(p1.get('login'), "collectiveidea")