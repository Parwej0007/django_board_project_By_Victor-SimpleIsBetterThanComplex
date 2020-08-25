from django.db import models
from django.db.models import Count
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model) :
    name = models.CharField(max_length=50, unique=True, null=True)
    description = models.CharField(max_length=100)
    def __str__(self) :
        return self.name

    def get_all_board(self):
        all_board = Board.objects.prefetch_related() \
            .annotate(post_count=Count('topic__post', distinct=True)) \
            .annotate(topic_count=Count('topic', distinct=True))
        return all_board

    def get_last(self) :
        return Post.objects.filter(topic__board=self).order_by('-updated_at').first()

    def get_topic(self):
        return Topic.objects.filter(board=self)

class Topic(models.Model) :
    topic_subject = models.CharField(max_length=100, blank=True)
    last_update = models.DateTimeField(auto_now_add=True)
    topic_stater = models.ForeignKey(User, related_name='topics', related_query_name='topic', on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name='topics', related_query_name='topic', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.topic_subject)

class Post(models.Model) :

    message = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='posts', related_query_name='post', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='posts_updated', related_query_name='post_updated', on_delete=models.CASCADE , null=True)
    topic = models.ForeignKey(Topic, related_name='posts', related_query_name='post', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.message)


