from django.contrib import admin

# Register your models here.
from .models import Music, User, Singer, Role, Vote, Transaction, Album

admin.site.register(Music)
admin.site.register(User)
admin.site.register(Singer)
admin.site.register(Role)
admin.site.register(Vote)
admin.site.register(Transaction)
admin.site.register(Album)