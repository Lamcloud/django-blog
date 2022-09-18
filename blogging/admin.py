from django.contrib import admin

from blogging.models import Post, Category

class MembershipInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]

class CategoryAdmin(admin.ModelAdmin):

    exclude = ('posts',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)


# from django.contrib import admin
#
# from blogging.models import Post, Category
#
# # and a new admin registration
# admin.site.register(Post)
#
# class CategoryAdmin(admin.ModelAdmin):
#     fields = ['name', 'description']
#
# class CategoryAdmin(admin.ModelAdmin):
#     exclude = ['posts']
#
# admin.site.register(Category, CategoryAdmin)

