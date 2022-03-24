from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Settings(models.Model):
    contacts=models.CharField(_('contacts'),max_length=255,blank=True,null=True)
    address=models.CharField(_('address'),max_length=255,blank=True,null=True)
    email=models.CharField(_('email'),max_length=255,blank=True,null=True)
    history=models.CharField(_('history'),max_length=255,blank=True,null=True)
    carousel1 = models.ImageField(
        _('carousel1'), upload_to=nameFile, default="uploads/Content.png")
    carousel2 = models.ImageField(
        _('carousel2'), upload_to=nameFile, default="uploads/Content.png")
    carousel3 = models.ImageField(
        _('carousel3'), upload_to=nameFile, default="uploads/Content.png")
    class Meta:
        ordering = ["-id"]
