import bcrypt

def hashpassword(password : str):
    salt=bcrypt.gensalt()
    hash_pass = bcrypt.hashpw(
        password.encode("utf-8"),
        salt
    ).decode("utf-8")

    return hash_pass

def varify_password(
    normal_password : str,
    hash_password : str
):

    varify_pass = bcrypt.checkpw(
        normal_password.encode("utf-8"),
        hash_password.encode("utf-8")
    )

    return varify_pass