from django.db import models
# from accounts.models import CustomUser

from BookStore import settings


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    price = models.IntegerField()
    publisher = models.CharField(max_length=50)
    page_numbers = models.CharField(max_length=5)
    available_quantity = models.BooleanField()
    publication_date = models.DateField()
    edition = models.CharField(max_length=20)
    # format of the book like it's hardback
    format = models.CharField(max_length=20)
    image = models.ImageField(upload_to='templates/images', blank=True)
    summery = models.TextField(null=True, default='this is summery of book')
    translator = models.CharField(max_length=150, blank=True)

    def __unicode__(self):
        return self.title

    # def get_absolute_url(self):


class Genres(models.Model):
    genre_id = models.CharField(max_length=5)


class Comment(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.RESTRICT)
    customer_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)


class PublisherInfo(models.Model):
    name = models.CharField(max_length=50)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)