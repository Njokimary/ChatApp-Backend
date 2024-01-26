from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    body = db.Column(db.String)

# Define a function to create the app context and initialize the database
def create_app():
    with app.app_context():
        db.create_all()
        return app

# Route to get all messages
@app.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    result = []
    for message in messages:
        result.append({
            'id': message.id,
            'user_id': message.user_id,
            'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'body': message.body
        })
    return jsonify(result)

# Route to post a message
@app.route('/messages', methods=['POST'])
def post_message():
    data = request.json  

    user_id = data.get('user_id')
    timestamp = datetime.utcnow()  
    body = data.get('body')

    new_message = Message(user_id=user_id, timestamp=timestamp, body=body)

    db.session.add(new_message)
    db.session.commit()

    return jsonify({'message': 'Message posted successfully'})

if __name__ == '__main__':
    create_app().run(debug=True)
