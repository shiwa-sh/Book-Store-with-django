from django.db import models
from django.contrib.auth.models import AbstractUser
from books.models import Book


class Library(models.Model):
    fav_books = models.ForeignKey(Book, on_delete=models.CASCADE)


class Orders(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    STATUS = [
        ('IN_P', 'IN PROGRESS'),
        ('DEL', 'DELIVERED'),
        ('RET', 'RETURNED'),
        ('CA', 'CANCELED')
    ]
    state = models.CharField(max_length=4, choices=STATUS)


class CustomUser(AbstractUser):
    address = models.TextField()
    library = models.ForeignKey(Book, on_delete=models.CASCADE)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, blank=True)
