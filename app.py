from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
db = SQLAlchemy(app)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
