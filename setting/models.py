from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Brand(models.Model):
    BRSName = models.CharField(max_length=40)
    BRSDesc = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

        def __str__(self):
            return self.BRSName


class Veriant(models.Model):
    VARSName = models.CharField(max_length=40)
    VARSDesc = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _("Veriant")
        verbose_name_plural = _("Veriants")

        def __str__(self):
            return self.VARSName