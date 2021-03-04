from api.integrations.github import GithubApi
from django.test import TestCase



class GithubApiTest(TestCase):

    def test_get_organization(self):
        githubapi = GithubApi()

        p1 = githubapi.get_organization('collectiveidea')
        self.assertEquals(p1.get('login'), "collectiveidea")

        p1 = githubapi.get_organization('errfree')
        self.assertEquals(p1.get('login'), "errfree")

        p1 = githubapi.get_organization('engineyard')
        self.assertEquals(p1.get('login'), "engineyard")

        p1 = githubapi.get_organization('galaxycats')
        self.assertEquals(p1.get('login'), "galaxycats")
        
        p1 = githubapi.get_organization('wesabe')
        self.assertEquals(p1.get('login'), "wesabe")

        p1 = githubapi.get_organization('gumgum')
        self.assertEquals(p1.get('login'), "gumgum")

        p1 = githubapi.get_organization('teste')
        self.assertEquals(p1, None)

        p1 = githubapi.get_organization('collectiveidea')
        self.assertEquals(p1.get('login'), "collectiveidea")

        p1 = githubapi.get_organization('collectiveidea')
        self.assertEquals(p1.get('login'), "collectiveidea")

        p1 = githubapi.get_organization('abs33')
        self.assertEquals(p1, None)

        p1 = githubapi.get_organization('engineyard')
        self.assertEquals(p1.get('login'), "engineyard")

        p1 = githubapi.get_organization('wwxxx')
        self.assertEquals(p1, None)


    def test_get_organization_public_members (self):
        githubapi = GithubApi()

        p1 = githubapi.get_organization_public_members('collectiveidea')
        self.assertEquals(p1, 5)

        p1 = githubapi.get_organization_public_members('errfree')
        self.assertEquals(p1, 0)

        p1 = githubapi.get_organization_public_members('engineyard')
        self.assertEquals(p1, 0)

        p1 = githubapi.get_organization_public_members('galaxycats')
        self.assertEquals(p1, 2)
        
        p1 = githubapi.get_organization_public_members('wesabe')
        self.assertEquals(p1, 2)

        p1 = githubapi.get_organization_public_members('gumgum')
        self.assertEquals(p1, 2)
