from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to simulate a database
books = [
    {"id": 1, "title": "Python Programming", "author": "John Doe"},
    {"id": 2, "title": "RESTful API Design", "author": "Jane Smith"},
]

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return "Book not found", 404
    return jsonify(book)

@app.route('/api/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if not data or 'title' not in data or 'author' not in data:
        return "Invalid data", 400
    new_book = {
        'id': len(books) + 1,
        'title': data['title'],
        'author': data['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return "Book not found", 404
    data = request.get_json()
    if not data or 'title' not in data or 'author' not in data:
        return "Invalid data", 400
    book['title'] = data['title']
    book['author'] = data['author']
    return jsonify(book)

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return "Book not found", 404
    books.remove(book)
    return "Book deleted", 200
@app.route('/', methods=['GET'])
def hello():
    return "Hello"

if __name__ == '_main_':
    app.run(debug=True)