from ninja import Schema
from datetime import date

class AuthorSchema(Schema):
    id: int
    name: str
    bio: str

class BookSchema(Schema):
    id: int
    title: str
    author_id: int
    isbn: str
    available_copies: int

class MemberSchema(Schema):
    id: int
    name: str
    email: str

class LoanSchema(Schema):
    id: int
    book_id: int
    member_id: int
    borrowed_date: date
    due_date: date
