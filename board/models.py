from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    image = models.FileField(upload_to="images/%Y/%m/%d", default='https://image.flaticon.com/icons/svg/149/149852.svg')
    post_hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

    # property를 사용하면 templates에서도 사용 가능
    @property
    def update_counter(self):
        self.post_hit = self.post_hit + 1
        self.save()

class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, related_name='comments')   
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_body = models.CharField(max_length=50)
