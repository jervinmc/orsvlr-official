from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone
# Create your models here.


def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Book(models.Model):
    firstname=models.CharField(_('firstname'),max_length=255,blank=True,null=True)
    middlename=models.CharField(_('middlename'),max_length=255,blank=True,null=True)
    lastname=models.CharField(_('lastname'),max_length=255,blank=True,null=True)
    contact_number=models.CharField(_('contact_number'),max_length=255,blank=True,null=True)
    email=models.CharField(_('email'),max_length=255,blank=True,null=True)
    service_type=models.CharField(_('contact_number'),max_length=255,blank=True,null=True)
    date_start=models.DateField(_('date_start'),blank=True,null=True)
    date_end=models.DateField(_('date_end'),blank=True,null=True)
    descriptions=models.CharField(_('descriptions'),max_length=255,blank=True,null=True)
    code=models.CharField(_('code'),max_length=255,blank=True,null=True)
    subtype=models.CharField(_('subtype'),max_length=255,blank=True,null=True)
    package=models.CharField(_('package'),max_length=255,blank=True,null=True)
    mode_of_payment=models.CharField(_('mode_of_payment'),max_length=255,blank=True,null=True)
    price=models.CharField(_('price'),max_length=255,blank=True,null=True)
    transaction_date=models.CharField(_('transaction_date'),max_length=255,blank=True,null=True)
    to_pay=models.CharField(_('to_pay'),max_length=255,blank=True,null=True)
    cancellation_description=models.CharField(_('cancellation_description'),max_length=255,blank=True,null=True)
    promoCode=models.CharField(_('promoCode'),max_length=255,blank=True,null=True)
    # transaction_date = models.DateTimeField(
    #     _('transaction_date'))
    status=models.CharField(_('status'),max_length=255,blank=True,null=True)
    proofOfPayment = models.ImageField(
        _('proofOfPayment'), upload_to=nameFile, default="uploads/book.png")
    class Meta:
        ordering = ["-id"]
