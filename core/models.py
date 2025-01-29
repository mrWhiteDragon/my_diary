from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"

    def __str__(self):
        return self.title
