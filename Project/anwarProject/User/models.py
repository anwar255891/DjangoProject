from django.db import models

# Create your models here.
class user(models.Model):
    ''' User: first_name, last_name, email, password, username '''
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50)
    def __str__(self):
         return self.username
    

class post(models.Model):
    '''Post: user, text, created_at, updated_at'''
    user=models.ForeignKey(user,on_delete=models.CASCADE) 
    text=models.CharField(max_length=500)
    created_at=models.DateField(max_length=50)
    updated_at=models.DateField(max_length=50)
    
    def __str__(self):
        return self.user.username
