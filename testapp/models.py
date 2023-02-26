from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'tbl_user'

    def __str__(self):
        return f"{self.name} {self.email}"
# Create your models here.

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'tbl_member'

    def __str__(self):
        return f"{self.firstname} {self.lastname}"