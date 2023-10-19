from django.db import models


class SeriesDescription(models.Model):
    name = models.CharField(max_length=15, null=False)
    title = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=500, default='Empty')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.title and self.name:
            self.title = self.name
        super(SeriesDescription, self).save(*args, **kwargs)