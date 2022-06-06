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

    return 'uploadpend/{filename}'.format(filename=filename)


class AdPend(models.Model):
    price=models.DecimalField(_('price'),max_digits=20, decimal_places=2,default=0.0)
    quantity=models.IntegerField(_('quantity'),blank=True,null=True)
    label=models.CharField(_('label'),max_length=255,blank=True,null=True)
    book_id=models.CharField(_('book_id'),max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["id"]
