from django.contrib import admin
from django.forms import widgets

from ibtsocs.root.models import Post

class PostAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'message':
            kwargs['widget'] = widgets.Textarea
        return super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Post, PostAdmin)
