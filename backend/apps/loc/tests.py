from rest_framework.test import APITestCase
from rest_framework import status

from .models import Location, City, Country, Region


class CountryTests(APITestCase):
    def test_create_country(self):
        url = "/api/v1/country/"
        data = {"name": "Test"}
        
        response = self.client.post(url, data, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Country.objects.count(), 1)
        self.assertEqual(Country.objects.get().name, "Test")

class RegionTests(APITestCase):
    def test_create_region(self):
        url = "/api/v1/region/"

        country = Country.objects.create(name="TestCountry")
        data = {"name": "Test", "country": country.id}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Region.objects.count(), 1)
        self.assertEqual(Region.objects.get().name, "Test")
        self.assertEqual(Region.objects.get().country, country)


class CityTests(APITestCase):
    def test_create_city(self):
        url = "/api/v1/city/"

        country = Country.objects.create(name="TestCountry")
        region = Region.objects.create(name="TestRegion", country=country)
        data = {"name": "Test", "region": region.id}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(City.objects.count(), 1)
        self.assertEqual(City.objects.get().name, "Test")
        self.assertEqual(City.objects.get().region, region)


class LocationTests(APITestCase):
    def test_create_location(self):
        url = "/api/v1/location/"

        country = Country.objects.create(name="TestCountry")
        region = Region.objects.create(name="TestRegion", country=country)
        city = City.objects.create(name="TestCity", region=region)

        data = {"country": country.id, "region": region.id, "city": city.id}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Location.objects.count(), 1)
        self.assertEqual(Location.objects.get().country, country)
        self.assertEqual(Location.objects.get().region, region)
        self.assertEqual(Location.objects.get().city, city)

