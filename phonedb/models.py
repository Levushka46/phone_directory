from django.db import models


class PhoneNumberAbstract(models.Model):
    code = models.CharField(max_length=3)
    start_range = models.IntegerField()
    end_range = models.IntegerField()
    operator = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    gar_territory = models.CharField(max_length=255)
    inn = models.CharField(max_length=25)

    class Meta:
        abstract = True


class PhoneNumber(PhoneNumberAbstract):
    pass


class UpdatePhoneNumber(PhoneNumberAbstract):
    pass
