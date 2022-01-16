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


class Amenities(models.Model):
    name=models.CharField(_('name'),max_length=255,blank=True,null=True)
    descriptions=models.CharField(_('package'),max_length=255,blank=True,null=True)
    price=models.CharField(_('descriptions'),max_length=255,blank=True,null=True)

    class Meta:
        ordering = ["-id"]
