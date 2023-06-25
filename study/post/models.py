from django.db import models
from user.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.id

class Comment(models.Model):
    content = models.TextField()

    # 외래키
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    # 외래키
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # 다대다 (좋아요)
    like = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.id

