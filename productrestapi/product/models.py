from django.db import models

# Create your models here.
class product(models.Model):
    pname=models.CharField(max_length=30)
    pvendor=models.CharField(max_length=30)
    pmodel=models.CharField(max_length=30)
    pqty=models.IntegerField()
    pprice=models.FloatField()

    # prod=models.manager() #for custume manger insted of default (objects)

    class Meta:
        db_table='product'
        constraints=[models.UniqueConstraint(fields=['pname','pvendor'],name='uqnamevendor')]
        indexes=[models.Index(fields=["pname",'pvendor'])]

    def __str__(self):
        return self.pname


