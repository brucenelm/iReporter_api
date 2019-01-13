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

	#checks that a specific incident can be returned
	def test_get_one_red_flag(self):
		response = self.client.get('/api/v1/red-flags/2')

		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 200)
		self.assertEqual(data['data'],{'incidentid':2,
					 					'createdOn':'Thu, 29 Nov 2018 11:46:35 GMT',
					 					'createdBy':'Pan', 
					 					'type': 'red-flag',
					 					'location':'23.8,45.6',
					 					'image':'image',
					 					'video':'video',
					 					'status':'invesstgation',
					 					'comment':'weired'})



if __name__ == '__main__':
	unittest.main()
