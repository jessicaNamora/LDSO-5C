from django.contrib import admin


from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from app.models import UserProfile


# Register your models here.

from .forms import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = SignUpForm
	# class Meta:
	# 	model = SignUp



admin.site.register(SignUp, SignUpAdmin)



class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
