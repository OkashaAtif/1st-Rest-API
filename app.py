from flask import Flask, jsonify, request
app = Flask(__name__)

books=[
    {'id':1, 'title':'Book 1', 'author' : 'Author 1'},
    {'id':2, 'title':'Book 2', 'author' : 'Author 2'},
    {'id':3, 'title':'Book 3', 'author' : 'Author 3'},
    {'id':4, 'title':'Book 4', 'author' : 'Author 4'},
    {'id':5, 'title':'Book 5', 'author' : 'Author 5'}
]

@app.route("/",methods=['GET'])
def home_page():
    return "<h1>Home Page</h1>"

# route to get all books
@app.route("/books",methods=['GET'])
def get_books():
    return jsonify(books)

# route to get specific book by id
@app.route("/books/<int:book_id>", methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id']==book_id:
            return jsonify(book)
    return jsonify({'error': 'Book not Found'})

# route to add a new book
@app.route("/books",methods=['POST'])
def add_book():
    new_book={
        "id":request.json['id'],
        "title":request.json['title'],
        "author":request.json['author']
    }
    books.append(new_book)
    return jsonify({'message':"Book added Successfully"})

# route to update an existing book
@app.route("/books/<int:book_id>", methods=['PUT'])   
# an HTTP request method used in REST APIs, 
#to update an existing resource or create a new resource,
#if it does not already exist.
def update_book(book_id):
    for book in books:
        if book['id']==book_id:
            book["title"]=request.json["title"]
            book["author"]=request.json["author"]
            return jsonify({'message':"Book updated Successfully"})
    return jsonify({'error': 'Book not Found'})

# route to delete an existing book
@app.route("/books/<int:book_id>", methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id']==book_id:
            books.remove(book)
            return jsonify({'message':"Book deleted Successfully"})
    return jsonify({'error': 'Book not Found'})

if __name__=='__main__':
    app.run(debug=True)