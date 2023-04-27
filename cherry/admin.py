from django.contrib import admin

# Register your models here.
from cherry.models import *

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)

