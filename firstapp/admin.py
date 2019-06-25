from django.contrib import admin
from firstapp.models import UserProfileInfo, Topic, Webpage, AccessRecord, User

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(User)
