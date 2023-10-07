from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

    def __init__(self, id, title, author):
        self.title = title
        self.author = author


@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    book_list = []
    for book in books:
        book_list.append({'id': book.id, 'title': book.title, 'author': book.author})
    return jsonify({'books': book_list})

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get(id)
    if book:
        return jsonify({'id': book.id, 'title': book.title, 'author': book.author})
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books/<int:id>', methods=['POST'])
def create_book(id):
    data = request.get_json()
    print(data)
    result = Book.query.filter_by(id=id).first()
    if result:
        return jsonify({'message': "Video ID does exist"}), 409

    new_book = Book(id=id, title=data['title'], author=data['author'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book created successfully', 'id': new_book.id})

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    data = request.get_json()
    book.title = data['title']
    book.author = data['author']
    db.session.commit()
    return jsonify({'message': 'Book updated successfully', 'id': book.id})

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})


@app.route('/books/clear', methods=['DELETE'])
def clear_books():
    try:
        # Delete all records from the Book table
        db.session.query(Book).delete()
        db.session.commit()

        return jsonify({'message': 'All books have been cleared'}), 200
    except Exception as e:
        db.session.rollback()  # Rollback the transaction in case of an error
        return jsonify({'error': 'An error occurred while clearing books'}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)
