from django.contrib import admin
from blog.models import Post,Cpost,UserIntract,BlogComment
# Register your models here.
admin.site.register(Post)
admin.site.register(UserIntract)
admin.site.register((BlogComment))

@admin.register(Cpost)
class CpostAdmin(admin.ModelAdmin):
    class Media:
        js=('tinyInjct.js',)