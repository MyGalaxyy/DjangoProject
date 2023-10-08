from django.contrib import admin

from .models import *
from .form import RegisterForm, UserUpdateProfileForm
# Register your models here.

admin.site.register(tinksPost)
admin.site.register(TweetComment)
admin.site.register(BanUser)
admin.site.register(RemoveBan)
admin.site.register(ReportManagement)
admin.site.register(LikeTweet)


admin.site.site_title = 'Admin Panel'
admin.site.site_header='Admin Panel'
admin.site.index_title ='Site Yönetim'

class UserAdmin(admin.ModelAdmin):
    model:BlogUser
    list_display = (
       'username', 'id','first_name', 'last_name', 'email', 'role','isApproved', 'isBanned', 'is_active' 
    )
    list_filter = ("id", "isApproved", "isBanned", 'is_active')


admin.site.register(BlogUser,UserAdmin)


