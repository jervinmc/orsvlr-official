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

    return 'uplofaq/{filename}'.format(filename=filename)


class Faq(models.Model):
    question=models.CharField(_('question'),max_length=255,blank=True,null=True)
    answer=models.CharField(_('answer'),max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["id"]
