from django.contrib import admin
from .models import Post,Games,Reviews,Comment
from django_summernote.admin import SummernoteModelAdmin

    # Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('content',)

admin.site.register(Post, SomeModelAdmin)
admin.site.register(Games, SomeModelAdmin)
admin.site.register(Reviews, SomeModelAdmin)
admin.site.register(Comment)
