from django.test import TestCase
from lettings.models import Letting, Address
from profiles.models import Profile
from django.contrib.auth.models import User


class TestSetUp(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            username='username1', 
            first_name='first_name1', 
            last_name='last_name1',
            email='username1@test.com',
            password='test1234'
        )
        self.user2 = User.objects.create(
            username='username2', 
            first_name='first_name2', 
            last_name='last_name2',
            email='username2@test.com',
            password='test1234'
        )
        self.user3 = User.objects.create(
            username='username3', 
            first_name='first_name3', 
            last_name='last_name3',
            email='username3@test.com',
            password='test1234'
        )
        self.profile1 = Profile.objects.create(
            user=self.user1, 
            favorite_city='Buenos Aires'
        )
        self.profile2 = Profile.objects.create(
            user=self.user2, 
            favorite_city='Budapest'
        )
        self.profile3 = Profile.objects.create(
            user=self.user3, 
            favorite_city='Barcelona'
        )
        self.address1 = Address.objects.create(
            number=7217,
            street='Bedford Street',
            city='Brunswick',
            state='GA',
            zip_code=31525,
            country_iso_code='USA'
        )
        self.address2 = Address.objects.create(
            number=4,
            street='Military Street',
            city='Willoughby',
            state='OH',
            zip_code=44094,
            country_iso_code='USA'
        )
        self.address3 = Address.objects.create(
            number=340,
            street='Wintergreen Avenue',
            city='Newport News',
            state='VA',
            zip_code=23601,
            country_iso_code='USA'
        )
        self.letting1=Letting.objects.create(
            title='Joshua Tree Green Haus /w Hot Tub', 
            address=self.address1
        )
        self.letting2=Letting.objects.create(
            title='Oceanview Retreat', 
            address=self.address2
        )
        self.letting3=Letting.objects.create(
            title="'Silo Studio' Cottage", 
            address=self.address3
        )