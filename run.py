from flask import Flask, request,jsonify
import datetime

app = Flask(__name__)

#list of users
list_of_users =[
{'userid':1,'firstname':'Peter','lastname':'Pan', 'othername': 'Greg','email':'peter@gmail.com','phoneNumber':'0774985635'},
{'userid':2,'firstname':'Mary','lastname':'Jane', 'othername': 'Jay','email':'mary@gmail.com','phoneNumber':'0774985645'},
]

#list of incidents
list_of_incidents =[{'incidentid':1,
					'createdOn':'Thu, 29 Nov 2018 11:46:35 GMT',
					'createdBy':'Pan', 
					'type': 'red-flag',
					'location':'23.8,45.6',
 					'image':'image',
 					'video':'video',
 					'status':'investgation',
 					'comment':'comments'},

 					{'incidentid':2,
 					'createdOn':'Thu, 29 Nov 2018 11:46:35 GMT',
 					'createdBy':'Pan', 
 					'type': 'red-flag',
 					'location':'23.8,45.6',
 					'image':'image',
 					'video':'video',
 					'status':'invesstgation',
 					'comment':'weired'},

 					{'incidentid':3,
 					'createdOn':'Thu, 29 Nov 2018 11:46:35 GMT',
 					'createdBy':'Ben', 
 					'type': 'red-flag',
 					'location':'57.5,7.9',
 					'image':'image',
 					'video':'video',
 					'status':'invesstgation',
 					'comment':'weired'}
]


#display list
display_list =[]

#returns all the incidents
@app.route('/api/<version>/red-flags', methods = ['GET'])
def get_red_flags(version):
	 
	return jsonify({'status':200,'data':list_of_incidents})


if __name__ == "__main__":
	app.run(debug=True)
