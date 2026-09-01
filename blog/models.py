from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Tags(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class User(models.Model):
    name = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.name} id, {self.id}"

    class Meta:
        ordering = ['id']

class Profile(models.Model):
    phone = models.CharField(max_length=20)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user}"

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to="blog_images/", null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs', null=True, blank=True)

    def __str__(self):
        return f"{self.name}, id = {self.id}"

    class Meta:
        verbose_name = "Blog"
        ordering = ['id']

class Blog_details(models.Model):
    duration = models.IntegerField()
    language = models.CharField(max_length=100)
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, related_name='details', null=True, blank=True)

    def __str__(self):
        return f"{self.blog.name if self.blog else 'N/A'}"