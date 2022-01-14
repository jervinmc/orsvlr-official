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


class Book(models.Model):
    customer_name=models.CharField(_('customer_name'),max_length=255,blank=True,null=True)
    contact_number=models.CharField(_('contact_number'),max_length=255,blank=True,null=True)
    email=models.CharField(_('email'),max_length=255,blank=True,null=True)
    service_type=models.CharField(_('contact_number'),max_length=255,blank=True,null=True)
    date_start=models.DateField(_('date_start'),blank=True,null=True)
    date_end=models.DateField(_('date_end'),blank=True,null=True)
    descriptions=models.CharField(_('descriptions'),max_length=255,blank=True,null=True)
    code=models.CharField(_('code'),max_length=255,blank=True,null=True)
    mode_of_payment=models.CharField(_('mode_of_payment'),max_length=255,blank=True,null=True)
    price=models.CharField(_('price'),max_length=255,blank=True,null=True)
    status=models.CharField(_('status'),max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["-id"]
