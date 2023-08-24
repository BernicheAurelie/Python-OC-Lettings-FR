import pytest
from django.test import TestCase
from django.template.loader import (
    render_to_string,
)
from oc_lettings_site.views import index
from profiles.views import (
    index as profiles_index,
)
from lettings.views import (
    index as lettings_index,
)
from django.urls import resolve


@pytest.mark.django_db
class TestUrls(TestCase):
    """
    class to check that urls are accessing and associated templates well returned
    """

    def test_index_view(self):
        """
        Unitary test for home page, check index() method is called on url '/'
        """
        found = resolve("/")
        self.assertEqual(found.func, index)

    def test_index(self):
        """
        Unitary test for home page,
        check well acces on url '/' and index template is returned
        """
        response = self.client.get("/")
        assert response.status_code == 200
        expected_html = render_to_string("index.html")
        self.assertEqual(
            response.content.decode(),
            expected_html,
        )
        assert (
            b'<h1 class="page-header-ui-title mb-3 display-6">Welcome to Holiday Homes</h1>'
            in response.content
        )
        assert b"Welcome to Holiday Homes" in response.content

    def test_get_profiles(self):
        """
        Unitary test for profiles page,
        check well acces on url '/profiles/' and profiles/index template is returned
        """
        response = self.client.get("/profiles/")
        assert response.status_code == 200
        expected_html = render_to_string("profiles/index.html")
        self.assertEqual(
            response.content.decode(),
            expected_html,
        )
        assert (
            b'<h1 class="page-header-ui-title mb-3 display-6">Profiles</h1>'
            in response.content
        )

    def test_get_profiles_index_view(
        self,
    ):
        """
        Unitary test for profiles page,
        check profiles index() method is called on url '/profiles/'
        """
        found = resolve("/profiles/")
        self.assertEqual(found.func, profiles_index)

    def test_get_lettings(self):
        """
        Unitary test for lettings page,
        check well acces on url '/lettings/' and lettings/index template is returned
        """
        response = self.client.get("/lettings/")
        assert response.status_code == 200
        expected_html = render_to_string("lettings/index.html")
        self.assertEqual(
            response.content.decode(),
            expected_html,
        )
        assert (
            b'<h1 class="page-header-ui-title mb-3 display-6">Lettings</h1>'
            in response.content
        )

    def test_get_lettings_index_view(
        self,
    ):
        """
        Unitary test for lettings page,
        check lettings index() method is called on url '/lettings/'
        """
        found = resolve("/lettings/")
        self.assertEqual(found.func, lettings_index)

    def test_wrong_url(self):
        response = self.client.get('/WrongUrl')
        expected_html = render_to_string("404.html")
        self.assertEqual(
            response.content.decode(),
            expected_html,
        )
        assert (
            b'Please check your letting id or you profile username, use link bellow' 
            in response.content
        )
    
    def test_wrong_letting(self):
        response = self.client.get('/lettings/50/')
        expected_html = render_to_string("404.html")
        self.assertEqual(
            response.content.decode(),
            expected_html,
        )
        assert (
            b'Please check your letting id or you profile username, use link bellow' 
            in response.content
        )
    
    def test_wrong_profile(self):
        response = self.client.get('/profiles/wrong_profile/')
        expected_html = render_to_string("404.html")
        self.assertEqual(
            response.content.decode(),
            expected_html,
        )
        assert (
            b'Please check your letting id or you profile username, use link bellow' 
            in response.content
        )