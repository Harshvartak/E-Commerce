from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(uplpad_to='images/', null=False)
    body=models.TextField()
    pub_date=models.DateTimeField(null=True)

    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%v %e %Y')
