from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

#
# # Unregister Groups.
admin.site.unregister(Group)


# Mix Profile Info User Info
class ProfileInline(admin.StackedInline):
    model = Profile


#
#
# # Extends User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", 'first_name', 'last_name', 'email']
    inlines = [ProfileInline]


#
#
# # Unregister initial User
admin.site.unregister(User)
# # Register User Profile
admin.site.register(User, UserAdmin)
