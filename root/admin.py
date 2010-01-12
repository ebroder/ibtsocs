from django.contrib import admin
from django.forms import widgets

from ibtsocs.root.models import Post, Vote

class PostAdmin(admin.ModelAdmin):
    list_display = ('short_message', 'nick', 'upvotes', 'downvotes', 'allvotes')

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'message':
            kwargs['widget'] = widgets.Textarea
        return super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Post, PostAdmin)
admin.site.register(Vote)
