from enum import Enum as PythonEnum

class UserRole(str, PythonEnum):
    USER = "user"
    ADMIN = "admin"

