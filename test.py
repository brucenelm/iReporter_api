import unittest
import run
import json
from flask_testing import TestCase
import datetime

class TestMainFlask(TestCase):

	def create_app(self):
		return run.app

	#checks that the number of incidents is more than 0
	def test_get_red_flags(self):
		response = self.client.get('/api/v1/red-flags')

		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 200)
		self.assertNotEqual(len(data['data']),0)


if __name__ == '__main__':
	unittest.main()
