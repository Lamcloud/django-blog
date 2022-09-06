from django.contrib import admin

from blogging.models import Post, Category

# and a new admin registration
admin.site.register(Post)
#admin.site.register(Category)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     pass
    #fields = ['category', 'title', 'text', 'author']

#admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'description']

class CategoryAdmin(admin.ModelAdmin):
    exclude = ['posts']

admin.site.register(Category, CategoryAdmin)

# class CategoryInline(admin.TabularInline):
#     model = Category
#
# class PostAdmin(admin.ModelAdmin):
#     inlines = [
#         CategoryInline,
#     ]
#
# admin.site.register(Post, PostAdmin)