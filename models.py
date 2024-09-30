from flask_sqlalchemy  import  SQLAlchemy

db = SQLAlchemy()

class User():
    __tablename__="users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    

