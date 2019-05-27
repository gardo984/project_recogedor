from django.db import models
from django.utils import timezone

# Create your models here.


class CommonStructure(models.Model):
    fregistro = models.DateField(
        null=False, default=timezone.now, blank=False)
    fhregistro = models.DateTimeField(
        null=True, default=timezone.now, blank=False)
    fhmodificacion = models.DateTimeField(
        null=True, default=None, blank=False)
    username = models.ForeignKey(
        'auth.User',
        null=True,
        on_delete=models.SET_NULL,
        default=None, blank=False)

    username_modif = models.ForeignKey(
        'auth.User',
        null=True,
        on_delete=models.SET_NULL,
        default=None, blank=False,
        related_name="%(app_label)s_%(class)s_username_modif_set",
    )

    class Meta:
        abstract = True
