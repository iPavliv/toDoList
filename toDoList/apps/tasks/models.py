from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=30)
    description = models.TextField()


class Task(models.Model):
    task_text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    done = models.BooleanField(default=False)
    note = models.TextField()
