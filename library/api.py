from ninja import NinjaAPI
from .models import Book, Author, Member, Loan
from .schemas import BookSchema, AuthorSchema, MemberSchema, LoanSchema
from typing import List

api = NinjaAPI()

@api.get("/books", response=List[BookSchema])
def list_books(request):
    return Book.objects.all()

@api.post("/cbooks", response=BookSchema)
def create_book(request, book: BookSchema):
    author = Author.objects.get(id=book.author_id)
    book = Book.objects.create(**book.dict())
    return book
@api.post("/member", response=MemberSchema)
def create_member(request, member: MemberSchema):
    member= Member.objects.get(id=member.id)
    return member
@api.post("/lbooks", response=LoanSchema)
def lending_book(request, loan: LoanSchema):
    loan= Loan.objects.get(id=loan.id)
    return loan
# Similarly, define endpoints for authors, members, and loans
