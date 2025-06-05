from jose import jwt, JWTError 
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
import schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/user/login')

SECRET_KEY = 'kSDFn9-lh4Fsa8js8LsmASDnl329sdfGlsdf3dlsf'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 60 

# create access token
def create_access_token(data: dict): 
    encode_data = data.copy() 
    expire = datetime.utcnow() + timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
    encode_data.update({"exp": expire})

    encoded_jwt = jwt.encode(encode_data, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt 

# verify access token 
def verify_access_token(token: str, credential_exception): 
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'unauthorized access')
    id: str = payload.get('user_id')
    if not id: 
        raise credential_exception 
    token_data = schemas.TokenData(id=str(id))

    return token_data

# get current user 
def current_user(token: str = Depends(oauth2_scheme)): 
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'unauthorized access')
 
    return verify_access_token(token, credential_exception)