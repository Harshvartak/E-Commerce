from django.db import models
from django.contrib.auth.models import User
from Users.models import CustomUser


class Product(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to='images/', null=False)
    description=models.TextField()
    cost= models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    pub_date=models.DateTimeField(null=True)

    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)


    def __str__(self):
        return self.title



    def summary(self):
        return self.description[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%v %e %Y')
