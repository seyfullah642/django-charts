from django.db import models


class FacebookConversions(models.Model):
    conversion = models.IntegerField()
    platform = models.CharField(max_length=200)
    date = models.DateField()


    def __str__(self):
        return f'{self.conversion}-{self.platform}-{self.date}'


class AdobeConversions(models.Model):
    conversion = models.IntegerField()
    platform = models.CharField(max_length=200)
    date = models.DateField()
    

    def __str__(self):
        return f'{self.conversion}-{self.platform}-{self.date}'


class DCMConversions(models.Model):
    conversion = models.IntegerField()
    platform = models.CharField(max_length=200)
    date = models.DateField()


    def __str__(self):
        return f'{self.conversion}-{self.platform}-{self.date}'