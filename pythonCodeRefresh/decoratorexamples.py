user: dict[str, str] = {"username": "jose", "access_level": "guest"}


def get_admin_password():
    return "1234"


def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin access for {user['username']}"

    return secure_function


get_admin_password = make_secure(get_admin_password)
print(get_admin_password())
