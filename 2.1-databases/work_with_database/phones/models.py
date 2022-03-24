from django.template.defaultfilters import slugify
from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=200)
    release_date = models.CharField(max_length=10)
    lte_exists = models.BooleanField()
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)