from flask import Flask, request

import settings
from src.manager import create_new_user, get_user_by_email, update_password, delete_user


app = Flask(__name__)


@app.route('/') 
def index():
    return {"message": "Server is running"}


@app.route('/create_user', methods=['POST'])
def create_user():
    """
    This is a view function for creating a new user.
    :return:
    """
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    password = request.form.get('password')

    if not all([email, first_name, last_name, password]):
        return {"status": "failure", "message": "Please provide value for all fields"}
    
    return create_new_user(email, first_name, last_name, password)


@app.route('/get_user/<string:email>', methods=['GET'])
def get_user(email):
    """
    This is a view function for getting the user info by email.
    :return:
    """    
    return get_user_by_email(email)


@app.route('/update_password/<string:email>', methods=['PUT'])
def update_user_passowrd(email):
    """
    This is a view function for update user password.
    :return:
    """

    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')

    if old_password is None or new_password is None:
        return {"status": "failure", "message": "Please provide value for all fields"}
    
    return update_password(email, old_password, new_password)


@app.route('/delete_user/<string:email>', methods=['DELETE'])
def delete_user_by_email(email: str):
    """
    This is a view function for delete user by email.
    :return:
    """
    return delete_user(email)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=settings.SERVER_PORT, debug=False)
