from django.db import models
from django.db.models import TextField
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Product(models.Model):
    PRDName = models.CharField(max_length=100, verbose_name=_("product name"))
    PRDCategory = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    PRDBrand = models.ForeignKey('setting.Brand', on_delete=models.CASCADE,  blank=True, null=True)
    PRDDesc = models.TextField(verbose_name=_("product Description"))
    PRDPrice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("price"))
    PRDCost = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("cost"))
    PRDCreated = models.DateTimeField(verbose_name=_("created At"))

    def __str__(self):
        return self.PRDName


class ProductImage(models.Model):
    PRDIProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("product"))
    PRDIImage = models.ImageField(upload_to='Product/', verbose_name=_("Image"))

    def __str__(self):
        return str(self.PRDIProduct)


class Category(models.Model):
    CATName = models.CharField(max_length=50)
    CATParent = models.ForeignKey('self', limit_choices_to={'CATParent__isnull': True}, on_delete=models.CASCADE,
                                  blank=True, null=True)
    CATDesc = models.TextField()
    CATImg = models.ImageField(upload_to='category/')

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return str(self.CATName)


class Product_Alternative(models.Model):
        PALNProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='main_product')
        PALNAlternatives = models.ManyToManyField(Product, related_name='alternative_product')

        class Meta:
            verbose_name = _("Product Alternative")
            verbose_name_plural = _("Product Alternatives")

        def __str__(self):
            return str(self.PALNProduct)


class Product_Accessories(models.Model):
        PACCProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='mainAccessories_product')
        PACCAlternatives = models.ManyToManyField(Product, related_name='Accessories_product')

        class Meta:
            verbose_name = _("Product Accessory")
            verbose_name_plural = _("Product Accessories")

        def __str__(self):
            return str(self.PACCProduct)
