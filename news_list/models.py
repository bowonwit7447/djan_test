from django.db import models

# Create your models here.
class News(models.Model):
    author = models.CharField(max_length=150, null=True)
    title = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    url = models.URLField(null=True)
    image_url = models.URLField(null=True)
    published_at = models.DateTimeField(null=True)
    # photo = models.ImageField(upload_to="gallery")

    def __str__(self):
        return '[ %s ] %s' % (self.published_at, self.title)
    