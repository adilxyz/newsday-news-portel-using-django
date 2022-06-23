from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = "categories"


    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=125)
    short_description = models.TextField()
    description = RichTextField()
    categories = models.ManyToManyField("web.Category")
    featured_image = models.ImageField(upload_to="news/")

    published_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "news"
        ordering = ["-id"]


    def __str__(self):
        return self.title