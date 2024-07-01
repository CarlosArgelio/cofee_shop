from django.db import models

class Car(models.Model):
    title = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)

    def __str__(self) -> str:
        return f"Car: {self.title} - Year: {self.year}"

class Publisher(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Author(models.Model):
    name = models.TextField(max_length=200)
    birt_date = models.DateField()

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name="authors")

    def __str__(self) -> str:
        return self.title
