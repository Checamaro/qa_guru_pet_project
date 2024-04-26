from dataclasses import dataclass

@dataclass
class User:
    user_email: str
    user_password: str
    user_first_name: str
    user_last_name: str
