from passlib.context import CryptContext 


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# create has password 

def hash_password(password: str): 

    return pwd_context.hash(password)

# verify hash password 

def verify_password(hashed_password, password: str): 

    return pwd_context.verify(hashed_password, password)