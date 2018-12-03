from flask import Flask
<<<<<<< HEAD
=======
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
>>>>>>> master
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
<<<<<<< HEAD


from app import routes
=======
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models
>>>>>>> master
