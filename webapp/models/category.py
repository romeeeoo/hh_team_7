from django.db import models


class Category(models.Model):
    name = models.CharField(blank=False, null=False, max_length=200)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

