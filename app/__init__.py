from flask import Flask
from .extensions import  db, migrate, login_manager
from .routes.user import user
from .routes.post import post
from .routes.student import student_bp

from .config import Config

def create_app(config_class=Config):
    app= Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(user)
    app.register_blueprint(post)
    app.register_blueprint(student_bp)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Login manager
    login_manager.login_view = 'user.login'
    login_manager.login_message = 'you are not logged in , you dont have access'
    login_manager.login_message_category = 'info'



    with app.app_context():
        db.create_all()

    return app