from django.contrib import admin
from.models import Newsletter,News,Fileupload,htmlupload,newshtmlupload

# Register your models here.
admin.site.register(Newsletter)
admin.site.register(News)
admin.site.register(Fileupload)
admin.site.register(htmlupload)
admin.site.register(newshtmlupload)
