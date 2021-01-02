from django.db import models


class FilterChoices(models.Model):
    company = models.TextField(null=True, verbose_name="Company", )
    product = models.TextField(null=True, verbose_name="Product", )
    parameter = models.TextField(null=True, verbose_name="Parameter", )
    values = models.TextField(null=True, verbose_name="Values", )



