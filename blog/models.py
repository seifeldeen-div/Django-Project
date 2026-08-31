from django.db import models


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to="blog_images/")

    def __str__(self):
        return f"{self.name}, id = {self.id}"

