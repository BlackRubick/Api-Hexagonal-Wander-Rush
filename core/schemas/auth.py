from pydantic import BaseModel


#validaciones de entrada
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str
