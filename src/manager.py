import peewee
from src.models import Users


def create_new_user(email, first_name, last_name, password):
    """
    This funcito is used to create a user with given email and password.
    :param email:
    :param first_name:
    :param last_name:
    :param password:
    :return:
    """
    try:
        Users.insert(email=email, first_name=first_name, last_name=last_name, password=password).execute()

    except peewee.IntegrityError:
        return {"status": "failure", "message": f"user already exists with email {email}"}

    except Exception as e:
        print(e)
        return {"status": "failure", "message": "Unexcepted error occured while creating user"}
    
    return {"status": "success", "message": f"User created successfully with email {email}"}


def get_user_by_email(email):
    """
    This function is used to get the user info by email.
    :param email:
    :return:
    """
    result = Users.select(Users.email, Users.first_name, Users.last_name).dicts().where(Users.email==email).execute()
    if not result:
        return {"status": "failure", "message": f"User not found with email {email}"}
    return {"status": "success", "data": {"first_name": result[0]["first_name"], "last_name": result[0]["last_name"]}}

def update_password(email, old_password, new_password):
    """
    This function is used to update password of the user.
    :param email:
    :param old_password:
    :param new_password:
    :return:
    """
    try:
        old_pswd = Users.get(Users.email == email).password
    except peewee.DoesNotExist:
        return {"status": "failure", "message": f"User not found with {email} email"}
    if old_pswd != old_password:
        return {"status": "failure", "message": "Old password didn't match"}
    
    try:
        Users.update(password=new_password).where(Users.email == email).execute()
        return {"status": "success", "message": f"Password updated successfully"}
    except Exception as e:
        return {"status": "failure", "message": "Unexcepted error occured in updating password"}

def delete_user(email):
    """
    This function is used to delete user by email.
    :param email:
    :return:
    """
    try:
        Users.get(Users.email == email).delete_instance()
        return {"status": "success", "message": f"User with {email} deleted successfully"}
    except peewee.DoesNotExist:
        return {"status": "failure", "message": f"User not found with {email}"}
