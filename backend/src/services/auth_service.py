import bcrypt
import datetime
import jwt

import config
from services.database_service import DatabaseService
from utils.error_codes import RegisterStatus, LoginStatus


class AuthService:
    def __init__(self):
        self.db_service = DatabaseService(config.ACCOUNT_DB_NAME)
        
    def __del__(self):
        self.db_service.close()

    def register(self, username, password):
        username = username.lower()
        if not username.isalnum():
            return RegisterStatus.USERNAME_INVALID
        if len(username) > 20:
            return RegisterStatus.USERNAME_TOO_LONG
        query = "SELECT * FROM users WHERE username = ?"
        args = (username,)
        if self.db_service.query(query, args):
            return RegisterStatus.USERNAME_TAKEN
        # check if password is valid sha256 hash
        if len(password) != 64 or not all(c in "0123456789abcdef" for c in password):
            return RegisterStatus.PASSWORD_INVALID
        hashed_password = bcrypt.hashpw(password.encode(), config.SALT)
        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        args = (username, hashed_password.decode())
        self.db_service.query(query, args)
        return RegisterStatus.SUCCESS

    def login(self, username, password):
        username = username.lower()
        query = "SELECT * FROM users WHERE username = ?"
        args = (username,)
        result = self.db_service.query(query, args)
        if not result:
            return LoginStatus.INVALID_CREDENTIALS, ''
        if not bcrypt.checkpw(password.encode(), result[0][2].encode()):
            self.log_login_attempt(username, False)
            return LoginStatus.INVALID_CREDENTIALS, ''
        else:
            self.log_login_attempt(username, True)        
            return LoginStatus.SUCCESS, create_token(result[0][0], result[0][1])
    
    def get_userid_from_username(self, username):
        query = "SELECT id FROM users WHERE username = ?"
        args = (username,)
        result = self.db_service.query(query, args)
        if not result:
            return -1
        else:
            return result[0][0]

    def log_login_attempt(self, username, status):
        user_id = self.get_userid_from_username(username)
        query = "INSERT INTO user_logins (user_id, success) VALUES (?, ?)"
        args = (user_id, status)
        self.db_service.query(query, args)

def create_token(user_id, username):
    exp = datetime.datetime.utcnow() + datetime.timedelta(hours=12)
    payload = {
        "user_id": user_id,
        "username": username,
        "exp": exp
    }
    token = jwt.encode(payload, config.JWT_SECRET, algorithm="HS256")
    return token


def verify_token(token):
    try:
        payload = jwt.decode(token, config.JWT_SECRET, algorithms=["HS256"])
        return True, payload["user_id"]
    except jwt.ExpiredSignatureError:
        return False, "Token has expired"
    except jwt.InvalidTokenError:
        return False, "Invalid token"
    except Exception as e:
        return False, str(e)