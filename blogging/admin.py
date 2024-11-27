from django.contrib import admin
from blogging.models import Post, Category

class CategoryInline(admin.TabularInline):  
    model = Category.posts.through
    extra = 1

class PostAdmin(admin.ModelAdmin):  
    list_display = ('title', 'author', 'published_date')
    list_filter = ('published_date',)
    search_fields = ('title', 'text')
    inlines = [CategoryInline]  

class CategoryAdmin(admin.ModelAdmin):  
    exclude = ('posts',)  

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
