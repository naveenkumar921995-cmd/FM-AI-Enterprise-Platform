SECRET_KEY = "FM_SECRET_KEY"


def authenticate(
        username,
        password
):

    if (
        username == "admin"
        and
        password == "admin123"
    ):
        return True

    return False