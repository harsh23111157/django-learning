from django.contrib import admin
from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display=('name','message')
  search_fields=('name','message')
  ordering=('name',)
  list_filter=('name','message')