from django.db import models
from django.core.validators import (
  EmailValidator,
  MaxValueValidator,
  MinValueValidator,
  URLValidator,
  validate_slug
)

from main.validators import (
  validate_even_number
)
#Create your models here.
#Every table in databases is represented as a class extended by models.Model class of django
#every row in a table is represented by an object of that class

class Student(models.Model):
  GENDERS = (
    ('f', 'Female'),
    ('m', 'Male'),
    ('o', 'Other')
  )

  # varchar(100)
  name = models.CharField(max_length = 100)
  # integer
  roll_number = models.IntegerField(unique = True)
  # Text
  # Can be null in db
  # cannot be null in ORM
  address = models.TextField(null = True)

  phone_number = models.CharField(max_length = 15, null = True, blank = True)
  # varchar(255)
  # validation only in ORM level
  email = models.CharField(max_length = 100, null = True, validators = [EmailValidator("Email address is not valid")])
  gender = models.CharField(max_length = 1, choices = GENDERS, null = True)

  age = models.IntegerField(
    null = True, 
    validators = [
      MaxValueValidator(150),
      MinValueValidator(0),
      validate_even_number
    ]
  )

  slug = models.CharField(max_length = 100, validators = [validate_slug], null = True)