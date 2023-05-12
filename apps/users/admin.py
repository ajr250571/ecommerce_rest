from django.contrib import admin
from apps.users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  #fields = [("url", "title"), "content"]
  list_display = ('username','last_name','name','email',)
  list_filter = ('last_name',)
  readonly_fields = ('password',)
  # exclude = ('password',)
  # search_fields = ('',)
  ordering = ('name',)

  