from fastapi import FastAPI
from config.database import Base, engine
from middlewares.error_handler import ErrorHandler

# ROUTERS IMPORTS
from routers.UsersRouter import users_router
from routers.UtilRouter import auth_router
from routers.RolesRouter import roles_router


# APPLICATION DATA
app = FastAPI()
app.title = "JW Secretary"
app.version = "0.0.1"

# MIDDLEWARE
app.add_middleware(ErrorHandler)

# ROUTERS
app.include_router(users_router)
app.include_router(roles_router)
app.include_router(auth_router)

# CREATE TABLES
Base.metadata.create_all(bind=engine)
