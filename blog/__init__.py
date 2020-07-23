from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_misaka import Misaka
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
Misaka(app)

# aggiungiamo il parametro render_as_batch=True se l'applicazione sta utilizzando sqlite
# perché alcune operazioni non sono ammesse in questo database e per ovviare a questo problema
# e per apportare delle modifiche allo scheda del database, viene creato un clone della tabella
# che stiamo modificando con l'aggiunta delle modifiche
with app.app_context():
    if db.engine.url.drivername == 'sqlite':
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

from blog import models, routes
