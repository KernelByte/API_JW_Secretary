from fastapi.security import HTTPBearer
from starlette.requests import Request
from util.jwt_manager import validate_token
from fastapi import  HTTPException

class JWTBearer(HTTPBearer):
      async def __call__(self, request: Request):
            auth = await super().__call__(request)
            data = validate_token(auth.credentials)
            if data['email'] != "adminejemplo@gmail.com":
                  raise HTTPException(status_code=403,detail="Credenciales invalidas")