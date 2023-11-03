from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField( max_length=200, unique=True)
    body = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_time = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name="post_like",blank=True,null=True)

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-pub_time',]
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        # get_latest_by = 'id'


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="commenters",on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment[:10]
    
    class Meta:
        ordering = ['-created_at',]
        verbose_name = 'comment'
        verbose_name_plural = 'comments'