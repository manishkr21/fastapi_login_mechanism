from fastapi import APIRouter, Depends, HTTPException, status, Request as Request2
from repository import database, models
from repository.hashing import Hash
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(
    tags=['Authentication']
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

templates = Jinja2Templates(directory="templates")


# method to store session data
@router.post('/login/')
def login(request:Request2, form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()

    if not user:
        raise HTTPException(status_code=401, detail=f'Invalid Credentials')
    
    if not Hash.verify(user.password, form_data.password):
        raise HTTPException(status_code=404, detail=f'Incorrect Password')

    # Store user data in the session
    request.session["user"] = {"username": user.username}

    return {"user": user.username}


# Route to render an HTML form for login
@router.get("/login/", response_class=HTMLResponse)
async def login_form(request: Request2):
    return templates.TemplateResponse("login.html", {"request": request})


# Route to get the current session data
@router.get("/get_user/")
def getusr(request: Request2):
    return request.session.get("user")


# Route to delete the session data
@router.get("/logout/")
def logout(request: Request2):
    request.session.clear()
    return {"message":"Logged out successfully"}
