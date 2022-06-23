from django.contrib import admin

from web.models import Category, News


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
admin.site.register(Category, CategoryAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "published_date"]
admin.site.register(News, NewsAdmin)
