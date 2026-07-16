from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display=('name','age','city')
  list_filter=('name','age')
  search_fields=('name','age','city')
  ordering=('name',)

  
  