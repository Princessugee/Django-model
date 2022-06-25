

from django.contrib.auth.models import get_user_model
from typing import Text
from django.db import models 



Author = get_user_model()

class blog(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField
    Author = models.ForeignKey(Author)
    def __str__(Author):
        
        return Author

      
    Created_date = models.DateTimeField()

    Published_date = models.DateTimeField()
    

  
