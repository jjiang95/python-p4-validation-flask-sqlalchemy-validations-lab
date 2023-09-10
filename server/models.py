from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError
        existing_author = Author.query.filter(Author.name == name).first()
        if existing_author and existing_author.id != self.id:
            raise ValueError
        return name
    
    @validates('phone_number')
    def validate_phone(self, key, number):
        if len(number) != 10:
            raise ValueError
        return number

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validate_title(self, key, title):
        if not title:
            raise ValueError
        if "Won't Believe" not in title or "Secret" not in title or "Top" not in title or "Guess" not in title:
            raise ValueError
        return title    

    @validates('content')
    def validate_content(self, key, content):
        if len(content) < 250:
            raise ValueError
        return content
    
    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) >= 250:
            raise ValueError
        return summary
    
    @validates('category')
    def validate_category(self, key, category):
        if category != "Fiction" and category != "Non-Fiction":
            raise ValueError
        return category
    
    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
