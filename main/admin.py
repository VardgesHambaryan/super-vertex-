from django.contrib import admin
from .models import Blog , OurServices , Gallery , ContactUs, HomeBg


@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'post_date' , 'img_preview']
    list_display_links = ['id' , 'title' , 'post_date', 'img_preview']
    search_fields = ['id' , 'title' , 'post_date' , 'text']

admin.site.register(OurServices)
admin.site.register(Gallery)
admin.site.register(ContactUs)
admin.site.register(HomeBg)




