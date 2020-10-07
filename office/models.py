from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class OfficeModel(models.Model):
    class Meta:
        db_table = 'office'

    name = models.CharField(max_length=20,
                            validators=[RegexValidator('^([a-zA-Z]{2,20})$', 'only a-z and A-Z min-3 max-20')])
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class EmployeeModel(models.Model):
    class Meta:
        db_table = 'employee'

    name = models.CharField(max_length=20,
                            validators=[RegexValidator('^([a-zA-Z]{2,20})$', 'only a-z and A-Z min-3 max-20')])
    age = models.IntegerField()
    city = models.CharField(max_length=20)

    # one to one
    # office = models.OneToOneField(OfficeModel, on_delete=models.CASCADE,related_name='employee')
    # many to many
    # offices = models.ManyToManyField(OfficeModel, related_name='employees',db_table='office_employee')
    # one to many
    office = models.ForeignKey(OfficeModel, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
