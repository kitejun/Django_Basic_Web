from django.db import models

class CRUD_Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField('date pulished')
    body = models.TextField()

    def __str__(self):
        return self.title
    