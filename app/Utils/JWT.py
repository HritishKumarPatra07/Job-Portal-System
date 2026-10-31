from jose import jwt , JWTError
from datetime import datetime,timedelta,timezone


MY_SECRET_KEY = "Hritish-Kumar-Patra"
ALGORITHM = "HS256"

def create_token(
    user_id:int,
    role:str
):
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    data = {
        "user_id":user_id,
        "role":role,
        "expire": int(expire.timestamp())
    }

    token = jwt.encode(
        data,
        MY_SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token

def varify_token(
    token:str
):
    try:

        data = jwt.decode(
            token,
            MY_SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return data

    except JWTError:
        return None


