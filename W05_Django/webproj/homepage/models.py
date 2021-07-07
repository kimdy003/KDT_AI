from django.db import models

# Create your models here.
#class <모델 이름>(models.Model):

class Coffee(models.Model):  # row
    # Field 1, 2, 3, ... (column)
    '''
    FieldTypes
    문자열 : CharField
    숫자 : IntegerFiedl, SmallIntegerField ...
    논리형 : BooleanField
    시간 / 날짜 : DataTimeField
    
    '''
    def __str__(self):
        return self.name

    name = models.CharField(default="", max_length=30)
    price = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=False)
    
