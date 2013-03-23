from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255)
    message = models.TextField()

    def __unicode__(self):
        return self.name

