from django.contrib import admin

from django.contrib import admin
from .models import BucketList

from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ('user',)

# Register your models here.
admin.site.register(BucketList)
