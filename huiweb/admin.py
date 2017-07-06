from django.contrib import admin
from huiweb.models import *
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(PDFPath,PDFPathAdmin)
