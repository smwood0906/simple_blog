from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def post_upload_handler(instance, filename):
    return"{slug}/img/{file}".format(slug=instance.slug, file=filename)

class Post(models.Model):
    content = models.TextField()
    date_created = models.DateTimeField(auto_now= True)
    title = models.CharField(max_length= 300)
    author = models.ForeignKey(User)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to= post_upload_handler)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"