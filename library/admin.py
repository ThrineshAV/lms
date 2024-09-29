from django.contrib import admin
from django.contrib import admin
from django.contrib import admin
from .models import Author, Book, Member, Loan

# Customize Author display in the admin panel
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')  # Fields to display in the list view
    search_fields = ('name',)       # Add search functionality

# Customize Book display
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'available_copies')
    search_fields = ('title', 'isbn')
    list_filter = ('author',)       # Add filter options

# Customize Member display
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','member_ship','contact_number')
    search_fields = ('name', 'email','contact_number')

# Customize Loan display
class LoanAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'lended_date', 'due_date','retrun_date','fine','status')
    list_filter = ('lended_date', 'due_date','status')

# Register the models with custom admin classes
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Loan, LoanAdmin)


# Register your models here.
