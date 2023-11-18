from django.contrib import admin

from log.models import Logl

class  res(admin.ModelAdmin):
    list_display=('level','message','resourceId','timestamp','traceId','spanId','commit','parentResourceId')


admin.site.register(Logl,res)

# Register your models here.
