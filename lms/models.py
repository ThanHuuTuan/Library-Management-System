from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=200)
    email_add = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    student_id = models.IntegerField(max_length=10)
    status = models.BooleanField()


    def __str__(self):
        return self.user_name


class Book_Issue(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_id = models.IntegerField(max_length=8)
    issue_date = models.DateTimeField('issue date')
    return_date = models.DateTimeField('return date')
    fine_amount = models.IntegerField(default=0)


    def __str__(self):
        return self.issue_date


class Books_Details(models.Model):
    book_code = models.ForeignKey(Book_Issue, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=60)
    catagory = models.CharField(max_length=20)
    auther_name = models.CharField(max_length=20)
    book_edition = models.IntegerField(default=1)


    def __str__(self):
        return self.book_title

