from flask import Flask
from config import Config
from database import db
from routes import app_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(app_routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создаём таблицы в БД
    app.run(debug=True)
