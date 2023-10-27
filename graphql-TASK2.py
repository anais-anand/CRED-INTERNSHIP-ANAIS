from flask import Flask, request, jsonify
from flask_graphql import GraphQLView
import graphene

app = Flask(__name__)

# Sample data to simulate a database
books = [
    {"id": 1, "title": "Python Programming", "author": "John Doe"},
    {"id": 2, "title": "RESTful API Design", "author": "Jane Smith"},
]

class Book(graphene.ObjectType):
    id = graphene.Int()
    title = graphene.String()
    author = graphene.String()

class Query(graphene.ObjectType):
    books = graphene.List(Book)
    book = graphene.Field(Book, id=graphene.Int())

    def resolve_books(self, info):
        return books

    def resolve_book(self, info, id):
        return next((book for book in books if book['id'] == id), None)

class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        author = graphene.String()

    book = graphene.Field(Book)

    def mutate(self, info, title, author):
        new_book = {
            'id': len(books) + 1,
            'title': title,
            'author': author
        }
        books.append(new_book)
        return CreateBook(book=new_book)

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)
