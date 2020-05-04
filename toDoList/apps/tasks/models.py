from django.db import models


class Category(models.Models):
    category_name = models.CharField()
    description = models.TextField()


class Task(models.Model):
    task_text = models.TextField()
    category = models.ForeignKey(Category)
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    done = models.BooleanField()
    note = models.TextField()
