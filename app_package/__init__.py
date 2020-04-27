from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app_package.config import Config

app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate=Migrate(app,db)

from app_package import main_route, admin_routes, emp_routes, auth
