from django.contrib import admin
from django.db import models

from api.models import Product

# Register your models here.
admin.site.register([
 Product
])
