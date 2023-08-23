import pytest
from tests.fixture import TestSetUp
from lettings.views import letting
from django.urls import resolve

pytestmark = pytest.mark.django_db

@pytest.mark.django_db
class TestProfiles(TestSetUp):
    databases = {'default'}

    def test_get_lettings_view(self):
        '''
        On vérifie que la méthode letting() est bien invoquée 
        sur /letting/<int:letting_id>/
        '''
        found = resolve('/lettings/'+ str(self.letting1.id) +'/')
        self.assertEqual(found.func, letting)

    def test_get_letting_template(self):
        response = self.client.get('/lettings/'+ str(self.letting1.id) +'/')
        assert self.letting1.title in response.content.decode()
        assert self.letting1.address.street in response.content.decode()
        assert str(self.letting1.address.zip_code) in response.content.decode()
        assert self.letting1.address.country_iso_code in response.content.decode()
        assert self.letting1.address.state in response.content.decode()
        assert str(self.address1.number) in response.content.decode()
        # renvoie adress: self.address1
        
        

    def test_letting_model(self):
        self.assertEqual(self.letting1.address.street, self.address1.street)
        self.assertEqual(self.letting1.address, self.address1)
        self.assertEqual(str(self.letting1), self.letting1.title)

    def test_address_model(self):
        self.assertEqual(str(self.address1), f'{self.address1.number} {self.address1.street}')
        # expected_address_street = self.address1.street
        # res_street = bytes(expected_address_street, 'utf-8')
        # assert res_street in response.content
        # assert b'<p>{{ address.number }} {{ address.street }}</p>' in response.content
    