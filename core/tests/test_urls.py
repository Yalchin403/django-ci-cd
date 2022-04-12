from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import hello


# adding simple test cases


class TestUrl(SimpleTestCase):
	def test_main_url(self):
		url = reverse("core:hello")
		self.assertEqual(resolve(url).func, hello)

	def test_fail_deliberate(self):
		assert 2 + 2 == 5
