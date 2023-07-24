import time
from typing import Dict
import jwt
from decouple import config
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # add this line

def token_response(token: str):
    return {
        "access_token": token
    }

def signJWT(user_email: str) -> Dict[str, str]:
    payload = {
        "user_email": user_email,
        "expires": time.time() + 86400
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}

def get_current_user_email(token: str = Depends(oauth2_scheme)) -> str:
    payload = decodeJWT(token)
    if payload is None or payload["user_email"] is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    return payload.get("user_email")
