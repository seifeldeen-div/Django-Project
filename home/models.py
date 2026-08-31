from django.db import models

# Create your models here. >>>> Sql
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to="blog_images/")
    # the diff between static files (dev) but dynamic upload files (user)

    