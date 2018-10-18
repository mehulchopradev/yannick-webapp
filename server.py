from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

fapp = Flask(__name__)
fapp.config.from_object(Config)
db = SQLAlchemy(fapp)
migrate = Migrate(fapp, db)

import models
import routes
