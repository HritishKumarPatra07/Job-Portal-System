from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException, status
from .JWT import varify_token
from jose import JWTError

oauth_schema = OAuth2PasswordBearer(tokenUrl=("/USER/login/"))

def current_user(
    token : str = Depends(oauth_schema)
):

    try:

        data = varify_token(token)

        if data is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

        return data
    
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
