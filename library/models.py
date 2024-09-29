from django.db import models

class Author(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly defining id
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly defining id
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    available_copies = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class Member(models.Model):
    mem=[
        ('premium','Premium'),
        ('basic','Basic'),
        ('free','Free'),
        ('student','Student')
    ]
    id = models.AutoField(primary_key=True)  # Explicitly defining id
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    member_ship=models.CharField(max_length=15,choices=mem,default='free')
    contact_number=models.CharField(max_length=10)
    

    def __str__(self):
        return self.name

class Loan(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly defining id
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    lended_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    retrun_date=models.DateField(null=True,blank=True)
    fine=models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    status_crr=[
        ('active','Active'),
        ('returned','Returned'),
        ('overdue','Overdue')
    ]
    status=models.CharField(max_length=10,choices=status_crr,default='active')

    def cal_fine(self):
        if self.retrun_date and self.retrun_date >self.due_date:
            fine = (self.due_date - self.retrun_date).days
            self.fine = fine * 100
        return 0
    def save(self,*args,**kwargs):
        self.fine=self.cal_fine()
        if self.retrun_date:
            if self.retrun_date >self.due_date:
                self.status='overdue'
            else:
                self.status='returned'
        super().save(*args,**kwargs)





    def __str__(self):
        return f"{self.book.title} loaned to {self.member.name}"

