from fastapi.security import OAuth2PasswordBearer

from app.core.database import SessionLocal

# db connection
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

# authorization 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

