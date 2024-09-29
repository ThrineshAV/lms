from ninja import NinjaAPI # type: ignore
from .models import Book, Author, Member, Loan
from .schemas import BookSchema, AuthorSchema, MemberSchema, LoanSchema
from typing import List

api = NinjaAPI()

@api.get("/books", response=List[BookSchema])
def list_books(request):
    # Serialize the queryset to a list of dictionaries
    return [BookSchema.from_orm(book) for book in Book.objects.all()]

@api.post("/cbooks", response=BookSchema)
def create_book(request, book: BookSchema):
    # Validate that the author exists
    author = Author.objects.filter(id=book.author_id).first()
    if not author:
        return {"error": "Author not found"}, 404  # Return an error if the author does not exist
    
    # Create and return the new book
    new_book = Book.objects.create(**book.dict())
    return BookSchema.from_orm(new_book)

@api.post("/member", response=MemberSchema)
def create_member(request, member: MemberSchema):
    # Create and return the new member
    new_member = Member.objects.create(**member.dict())
    return MemberSchema.from_orm(new_member)

@api.post("/lbooks", response=LoanSchema)
def lending_book(request, loan: LoanSchema):
    # Create and return the new loan
    new_loan = Loan.objects.create(**loan.dict())
    return LoanSchema.from_orm(new_loan)

# Similarly, define endpoints for authors, members, and loans
