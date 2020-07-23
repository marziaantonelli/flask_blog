import os

#locazione del progetto
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'blog.db')

    # serve per prevenire l'invio di segnali in fase di modifica di cui non abbiamo bisogno
    # mantenendo l'applicazione più veloce
    SQLALCHEMY_TRACK_MODIFICATIONS = False