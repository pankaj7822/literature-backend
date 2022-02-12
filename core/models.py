from django.db import models


class Literature(models.Model):
    title=models.CharField(max_length=500,null=True,blank=True)
    link=models.CharField(max_length=500,null=True,blank=True)
    remarks=models.CharField(max_length=500,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.title
