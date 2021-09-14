# user-account

This is a backend server for user-accounts in Python3.6 using Flask Framework. MySQL as a 
Database and Peewee ORM to communicate with the database.

# Server Setup

1. Create a virtual environment for this project. 
    python3.6 -m venv name_of_env

2. Activate virtual environment.
    source name_of_env/bin/activate

3. Install all dependencies in the virtual environment.
    python install -r requirements.txt

4. Set your database environment in settings.py file

5. Migrate database by migration.py file.
    python migration.py

6. Set port in settings.py and run server on localhost.
    python app.py

Now your server is running on localhost:port you can check it. 

# APIs to communicate with server.

This server is deployed on AWS. Check the server availability through this link https://ivwmzgg2wb.execute-api.ap-south-1.amazonaws.com/testing 

1. To create user go to this link.

    https://ivwmzgg2wb.execute-api.ap-south-1.amazonaws.com/testing/create_user

    This is an post API method. You have to provide email, first_name, last_name, and password in body form-data format.

2. To get the user info by email.
    This is a GET api method.
    https://ivwmzgg2wb.execute-api.ap-south-1.amazonaws.com/testing/get_user/{email}

3. To update user password.
    This is a PUT api method.
    https://ivwmzgg2wb.execute-api.ap-south-1.amazonaws.com/testing/update_password/{email}

    And provide old_password and new_password in body form-data format.

4. To delete user account.
    This is a DELETE api method.
    https://ivwmzgg2wb.execute-api.ap-south-1.amazonaws.com/testing/delete_user/{email}


# Postman collection
    https://www.getpostman.com/collections/fe6b656899ecef1e2f7c