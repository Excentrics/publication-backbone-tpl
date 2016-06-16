'''
from django.contrib import admin
from .models import TestEv

class TestEvAdmin(admin.ModelAdmin):
    model = TestEv

admin.site.register(TestEv, TestEvAdmin)
'''