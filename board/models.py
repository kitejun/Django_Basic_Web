from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    image = models.FileField(upload_to="images/%Y/%m/%d", default='https://image.flaticon.com/icons/svg/149/149852.svg')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

'''
class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    author = models.CharField(max_length=10)
    message = models.TextField()
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.author
'''