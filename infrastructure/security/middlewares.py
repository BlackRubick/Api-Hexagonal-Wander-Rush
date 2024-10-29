import jwt
from fastapi import Request, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_401_UNAUTHORIZED
from jose import JWTError, jwt
from core.utils.security import Security

security = Security()
#con esto controlamos la cantidad de peticiones


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, security.SECRET_KEY, algorithms=[security.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username
