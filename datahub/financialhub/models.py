from django.db import models


class Investment(models.Model):
    TYPE = (
        ('F', 'Fixed'),
        ('V', 'Variable')
    )
    name = models.CharField(max_length=50)
    monetary_value = models.DecimalField(max_digits=10, decimal_places=2)
    bank_name = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=TYPE,  blank=False, null=False)

    def __str__(self):
        return self.name
