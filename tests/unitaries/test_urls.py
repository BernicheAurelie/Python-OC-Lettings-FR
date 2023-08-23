import pytest
from django.test import TestCase
from django.template.loader import render_to_string
from oc_lettings_site.views import index
from profiles.views import index as profiles_index
from lettings.views import index as lettings_index
from django.urls import resolve
from django.http.request import HttpRequest

@pytest.mark.django_db
class TestUrls(TestCase):
    '''
    Test unitaire de la page accueil sur la racine du projet
    On vérifie que la méthode index() est bien invoquée sur /
    '''
    def test_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index(self):
        response = self.client.get('/')
        assert response.status_code == 200
        expected_html = render_to_string('index.html')
        self.assertEqual(response.content.decode(), expected_html)
        assert b'<h1 class="page-header-ui-title mb-3 display-6">Welcome to Holiday Homes</h1>' in response.content
        assert b'Welcome to Holiday Homes' in response.content

    def test_get_profiles(self):
        response = self.client.get('/profiles/')
        assert response.status_code == 200
        expected_html = render_to_string('profiles/index.html')
        self.assertEqual(response.content.decode(), expected_html)
        assert b'<h1 class="page-header-ui-title mb-3 display-6">Profiles</h1>' in response.content

    def test_get_profiles_index_view(self):
        '''
        Test unitaire de la page profiles du projet
        On vérifie que la méthode index() est bien invoquée sur /profiles/
        '''
        found = resolve('/profiles/')
        self.assertEqual(found.func, profiles_index)

    def test_get_lettings(self):
        response = self.client.get('/lettings/')
        assert response.status_code == 200
        expected_html = render_to_string('lettings/index.html')
        self.assertEqual(response.content.decode(), expected_html)
        assert b'<h1 class="page-header-ui-title mb-3 display-6">Lettings</h1>' in response.content

    def test_get_lettings_index_view(self):
        '''
        Test unitaire de la page lettings du projet
        On vérifie que la méthode index() est bien invoquée
        '''
        found = resolve('/lettings/')
        self.assertEqual(found.func, lettings_index)