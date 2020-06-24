## Live at: https://dry-woodland-82867.herokuapp.com/api/v1/users/
.

## Python packages used
* Python 3.6.9
* Django 3.0.6
* Postgres
* Django Rest Framework 3.11.0
* sqlparse 0.3.1
* gunicorn 20.0.4
* django-heroku 0.3.1
.

### Components of this app
* **Models**
1. User Model

	|User|
	---|
	user_id|
	real_name|
	timezone|

2. Activities Model (Many to one relationship with User Model)

	|Activity|
	---|
	user(Foreign Key)|
	start_time|
	end_time|

* **APIs**

	Convention followed - ``` /api/v1/{routes} ```
	1. Users (```/api/v1/users```)
	This API end-point accesses the database and retrives data for every user. It returns a JSON response containing the:
		1. user_id
		2. real_name
		3. tz
		4. activities:
			1. start_time
			2. end_time
	A response for a single user would look something like this: 
	
	```
	[
	    {
		"user_id": "YDCGASOOE",
		"real_name": "agni",
		"tz": "Indian/Chagos",
		"activities": [
		    {
			"start_time": "Jun 23 2020  18:34PM",
			"end_time": "Jun 30 2020  18:34PM"
		    },
		    {
			"start_time": "Jun 26 2020  18:35PM",
			"end_time": "Jun 27 2020  18:00PM"
		    },
		    {
			"start_time": "Jun 23 2020  21:36PM",
			"end_time": "Jun 23 2020  21:36PM"
		    }
		]
	    }
    ]
	```
	
	2. Activities (```/api/v1/activity/```)
	This APIs allows viewing all the added activities of different users and also add a new activity for any existing user(by selecting the user from a drop down menu) It returns a JSON reaponse containing the:
		1. user (user_id of the corresponding user)
		2. start_time
		3. end_time
	A typical response would look something like: 
	
	```
	[
		{
		"user": "YDCGASOOE",
		"start_time": "Jun 26 2020  18:35PM",
		"end_time": "Jun 27 2020  18:00PM"
	    },
	    {
		"user": "IIH2ATU6N",
		"start_time": "Jun 09 2020  18:36PM",
		"end_time": "Jun 29 2020  18:36PM"
	    }
	]
	```
* **Custom Management commands**

	```python manage.py populate number_of_reuired_users```

	This command is for creating required number of dummy users. Replace {number_of_reuired_users} with the required number.


### To run locally, do the usual:

* Create a Python 3.6 or above virtualenv
```python
    python -m venv venv
```
* Activate the virtualenv by:
```
    source venv/bin/activate
```

* Install dependencies:
```
    pip install -r requirements.txt
```

* Create User data:

	1. Using admin portal:
	
		```python manage.py createsuperuser```
		
		Then fill the required details and login to localhost:8000/admin using the previously given credentials and add users and activities as required.
		
	2. Using the management command:
	
		```python manage.py polulate 10```
		
		This creates 10 random users with random activity periods and stores them in the database.
	

* Start the server:
```
    python manage.py runserver
```

Goto ``` localhost:8000/api/v1/users ```


