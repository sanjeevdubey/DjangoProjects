from django.contrib import admin
from .models import Category, blog
from django.utils.html import format_html

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_title", "category_description","created_date","updated")
    fields = ("category_title", "category_description","created_date",)

class blogAdmin(admin.ModelAdmin):
    readonly_fields = ("show_featured_image",)
    list_display = ("blog_title", "cat_id", "showless_content","show_featured_image","is_deleted","created_date","displayclickbutton")
    list_display_links = ("showless_content","blog_title","displayclickbutton") #This with add link on the fields
    fields       = ("cat_id","blog_title", "blogtype",  "featured_image","blog_description","created_date","is_deleted") # to show the fileds
    #exclude      = ("is_deleted",)  # not to show the fileds
    #list_filter  = ("is_deleted",)
    radio_fields = {"blogtype":admin.HORIZONTAL}
    save_on_top = True
    list_per_page =10
    #To show content description less in word. Instead showing all description
    def showless_content(self,obj):
        #print(obj)
        return format_html(f'<p style="color:red">{obj.blog_description[0:100]}</p>')
    
    # to show the image of the fetured image uploaded
    def show_featured_image(self,obj):
        #print(obj)
        return format_html(f'<img width="50px" height="50px" src="{obj.featured_image.url}"/>')

    # Creating button to click
    def displayclickbutton(self, obj):
        return format_html(f'<a class="button" href="/admin/blogapp/blog/{obj.id}/change/">Edit</a>')    

admin.site.register(blog,blogAdmin)
admin.site.register(Category,CategoryAdmin)

