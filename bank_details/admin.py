from django.contrib import admin
from .models import Branches

@admin.register(Branches)
class UserAdmin(admin.ModelAdmin):
 list_display = ('ifsc', 'bank_id', 'branch', 'address','city','district','state','bank_name')



