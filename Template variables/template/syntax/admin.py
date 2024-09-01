from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname",)
  
admin.site.register(Member,MemberAdmin)