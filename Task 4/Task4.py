from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

db = SQLAlchemy(app)
jwt = JWTManager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = generate_password_hash(data.get('password'))

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully!'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()
    if user and check_password_hash(user.password, data.get('password')):
        token = create_access_token(identity=user.username)
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username} for user in users])

if __name__ == '__main__':
    app.run(debug=True)
    
   