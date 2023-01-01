from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=("title","short","is_active","created_at",)
    list_display_links=("title","short")
    readonly_fields=("created_at",)
    ordering=("-created_at",)

    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(Post, PostAdmin)
