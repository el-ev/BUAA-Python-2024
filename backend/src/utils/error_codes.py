from enum import Enum


class LoginStatus(Enum):
    LOGIN_SUCCESS = (0, "")
    # Frontend (and backend) errors
    USERNAME_EMPTY = (1, "Username cannot be empty.")
    PASSWORD_EMPTY = (2, "Password cannot be empty.")
    # Backend errors
    INVALID_CREDENTIALS = (3, "Invalid username or password.")
    UNKNOWN_ERROR = (4, "An unknown error occurred.")
    NETWORK_ERROR = (5, "Network error.")

    @classmethod
    def from_value(cls, value):
        for status in LoginStatus:
            if status.value[0] == value:
                return status
        return LoginStatus.UNKNOWN_ERROR

    @classmethod
    def get_error_message(cls, code):
        for error in cls:
            if error.value[0] == code.value[0]:
                return error.value[1]
        return cls.UNKNOWN_ERROR.value[1]

class RegisterStatus(Enum):
    REGISTER_SUCCESS = (0, "")
    # Frontend errors
    USERNAME_EMPTY = (1, "Username cannot be empty.")
    USERNAME_INVALID = (2, "Username can only contain letters and numbers.")
    USERNAME_TOO_LONG = (3, "Username is too long.")
    PASSWORD_EMPTY = (4, "Password cannot be empty.")
    PASSWORD_INVALID = (5, "Password does not satisfy requirements.")
    PASSWORDS_MISMATCH = (6, "Passwords do not match.")
    # Backend errors
    USERNAME_TAKEN = (7, "Username is already taken.")
    UNKNOWN_ERROR = (8, "An unknown error occurred.")
    NETWORK_ERROR = (9, "Network error.")

    @classmethod
    def from_value(cls, value):
        for status in RegisterStatus:
            if status.value[0] == value:
                return status
        return RegisterStatus.UNKNOWN_ERROR

    @classmethod
    def get_error_message(cls, code):
        for error in cls:
            if error.value[0] == code.value[0]:
                return error.value[1]
        return cls.UNKNOWN_ERROR.value[1]
    
class UploadFileStatus(Enum):
    UPLOAD_SUCCESS = (0, "")
    # Frontend errors
    FILENAME_EMPTY = (1, "Filename cannot be empty.")
    FILENAME_INVALID = (2, "Filename is invalid.")
    FILENAME_TOO_LONG = (3, "Filename is too long.")
    FILE_TOO_LARGE = (4, "File is too large.")
    # Backend errors
    UNAUTHORIZED = (5, "Unauthorized.")
    UNKNOWN_ERROR = (6, "An unknown error occurred.")
    NETWORK_ERROR = (7, "Network error.")

    @classmethod
    def from_value(cls, value):
        for status in UploadFileStatus:
            if status.value[0] == value:
                return status
        return UploadFileStatus.UNKNOWN_ERROR

    @classmethod
    def get_error_message(cls, code):
        for error in cls:
            if error.value[0] == code.value[0]:
                return error.value[1]
        return cls.UNKNOWN_ERROR.value[1]