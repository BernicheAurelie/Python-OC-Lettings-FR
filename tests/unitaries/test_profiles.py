import pytest
from tests.fixture import TestSetUp
from profiles.views import profile
from django.urls import resolve

pytestmark = pytest.mark.django_db

@pytest.mark.django_db
class TestProfiles(TestSetUp):
    databases = {'default'}

    def test_get_profiles_view(self):
        '''
        On vérifie que la méthode profile() est bien invoquée 
        sur /profiles/<str:username>/
        '''
        found = resolve('/profiles/'+ self.profile1.user.username +'/')
        self.assertEqual(found.func, profile)

    def test_get_profile_template(self):
        response = self.client.get('/profiles/'+ self.profile1.user.username +'/')
        assert b'<strong>First name :</strong>' in response.content
        assert b'<strong>Last name :</strong>' in response.content
        assert b'<strong>Email :</strong>' in response.content

    def test_get_a_profile(self, **kwargs):
        response = self.client.get('/profiles/'+ self.profile1.user.username +'/')
        self.assertEqual(response.status_code, 200)
        assert b'<h1 class="page-header-ui-title mb-3 display-6">username1</h1>' in response.content
        assert b'<p><strong>First name :</strong> first_name1</p>' in response.content
        assert b'<p><strong>Last name :</strong> last_name1</p>' in response.content
        assert b'<p><strong>Email :</strong> username1@test.com</p>' in response.content
        # convert string to byte
        favorite_city = self.profile1.favorite_city
        res = bytes(favorite_city, 'utf-8')
        assert res in response.content

    def test_profile_model(self):
        self.assertEqual(str(self.profile1), f'{self.user1.username}')
       
    
        