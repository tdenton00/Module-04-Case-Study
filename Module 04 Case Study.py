from flask import Flask, request, jsonify

app = Flask(__name__)


books = []


class Book:
    def __init__(self, id, book_name, author, publisher):
        self.id = id
        self.book_name = book_name
        self.author = author
        self.publisher = publisher


@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(id=data['id'], book_name=data['book_name'], author=data['author'], publisher=data['publisher'])
    books.append(new_book.__dict__)
    return jsonify(new_book.__dict__), 201


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200


@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book:
        return jsonify(book), 200
    return jsonify({'message': 'Book not found'}), 404


@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = next((book for book in books if book['id'] == id), None)
    if book:
        book['book_name'] = data.get('book_name', book['book_name'])
        book['author'] = data.get('author', book['author'])
        book['publisher'] = data.get('publisher', book['publisher'])
        return jsonify(book), 200
    return jsonify({'message': 'Book not found'}), 404


@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book['id'] != id]
    return jsonify({'message': 'Book deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
