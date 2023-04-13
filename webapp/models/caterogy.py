from django.db import models


class Category(models.Model):
    name = models.CharField(blank=False, null=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

