from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
from django.urls  import  reverse 
from users.models import User
class Category(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        db_table = 'Category'

    def __str__(self):
        return self.name


class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique_for_date='created', allow_unicode=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()  # 기본 매니져
    postObjects = PostObjects()  # 커스텀한 매니져

    class Meta:
        ordering = ('-created',)
        db_table = 'Post'
    

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post_detail', kwargs={'slug': self.slug})