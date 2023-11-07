from django.db import models
from django.urls import reverse


class Todo(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("todo_edit", kwargs={"pk": self.pk})
