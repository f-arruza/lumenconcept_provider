import uuid

from django.db import models


# Create your models here.
class Category(models.Model):
    code = models.CharField('Code', max_length=20)
    name = models.CharField('Name', max_length=50)
    description = models.TextField('Description', blank=True)
    active = models.BooleanField('Active', default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'provider_category'
        verbose_name_plural = 'Categories'


class Requirement(models.Model):
    name = models.CharField('Name', max_length=50)
    mandatory = models.BooleanField('Active', default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='requirements')
    active = models.BooleanField('Active', default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'provider_requirement'
        verbose_name_plural = 'Requirements'


class Provider(models.Model):
    code = models.UUIDField('Code', default=uuid.uuid4, editable=False)
    name = models.CharField('Name', max_length=50)
    description = models.TextField('Description', blank=True)
    address = models.CharField('Address', max_length=50)
    city = models.CharField('City', max_length=50)
    country = models.CharField('Country', max_length=50)
    email = models.EmailField('Email', max_length=50)
    phone = models.CharField('Phone', max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='providers')
    score = models.DecimalField('Score', max_digits=3, decimal_places=2,
                                default=0.00)
    active = models.BooleanField('Active', default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'provider'
        verbose_name_plural = 'Providers'


class Support(models.Model):
    description = models.TextField('Description', blank=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE,
                                 related_name='supports')
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE,
                                    related_name='req_supports')
    path = models.FileField('Path', upload_to='supports/')
    active = models.BooleanField('Active', default=True)

    def __str__(self):
        return self.provider.name + " " + self.requirement.name

    class Meta:
        db_table = 'provider_support'
        verbose_name_plural = 'Supports'


class Calification(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE,
                                 related_name='califications')
    value = models.DecimalField('Value', max_digits=3, decimal_places=2,
                                default=0.00)
    observation = models.TextField('Observation', blank=True)
    user = models.CharField('Country', max_length=36)

    def __str__(self):
        return self.provider.name + " " + self.user

    class Meta:
        db_table = 'provider_calification'
        verbose_name_plural = 'Califications'
