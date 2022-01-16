from django.contrib import admin
from jobapp.models import hydjobs,blorejobs,patnajobs,punejobs

# Register your models here.

class hydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','mobileno']

class blorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','mobileno']

class patnajobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','mobileno']

class punejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','mobileno']

admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(blorejobs,blorejobsAdmin)
admin.site.register(patnajobs,patnajobsAdmin)
admin.site.register(punejobs,punejobsAdmin)
