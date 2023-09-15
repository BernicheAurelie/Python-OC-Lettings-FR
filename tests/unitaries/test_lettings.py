import pytest
from tests.fixture import TestSetUp
from lettings.views import letting
from django.urls import resolve

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestProfiles(TestSetUp):
    """
    class that inherits from TestSetUp class so database is initialize with our created datas.
    """

    databases = {"default"}

    def test_get_lettings_view(self):
        """
        Test for a specific letting page,
        check lettings() method is called on url '/lettings/<int:letting_id>/'
        """
        found = resolve("/lettings/" + str(self.letting1.id) + "/")
        self.assertEqual(found.func, letting)

    def test_get_letting_template(self):
        """
        Test for a specific letting page,
        check well acces on url '/lettings/<int:letting_id>/'
        and lettings template is returned
        """
        response = self.client.get("/lettings/" + str(self.letting1.id) + "/")
        self.assertEqual(response.status_code, 200)
        # Profiles link, specific to this template
        assert (
            '<a class="btn fw-500 ms-lg-4 btn-primary px-10" href="/profiles/">'
            in response.content.decode()
        )

    def test_get_a_letting(self):
        """
        Test for a specific letting page,
        check url '/lettings/<int:letting_id>/'
        returned attendees datas on this specific letting.
        """
        response = self.client.get("/lettings/" + str(self.letting1.id) + "/")
        assert self.letting1.title in response.content.decode()
        assert self.letting1.address.street in response.content.decode()
        assert str(self.letting1.address.zip_code) in response.content.decode()
        assert self.letting1.address.country_iso_code in response.content.decode()
        assert self.letting1.address.state in response.content.decode()
        # return adress: self.address1
        assert str(self.address1.number) in response.content.decode()

    def test_letting_model(self):
        """Test to check letting return is letting's title
        and check the correct address is associated
        """
        self.assertEqual(
            self.letting1.address.street,
            self.address1.street,
        )
        self.assertEqual(
            self.letting1.address,
            self.address1,
        )
        self.assertEqual(
            str(self.letting1),
            self.letting1.title,
        )

    def test_address_model(self):
        """Test to check address return is address number and street"""
        self.assertEqual(
            str(self.address1),
            f"{self.address1.number} {self.address1.street}",
        )
