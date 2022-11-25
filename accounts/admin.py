from django.contrib import admin
from accounts.models import User, Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['fullname']

admin.site.register(User)
admin.site.register(Author, AuthorAdmin)
