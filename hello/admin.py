from django.contrib import admin

from hello.models import *

# Register your models here.

@admin.register(Publish)    # 方式二：使用register的装饰器
class PublishAdmin(admin.ModelAdmin):
    list_display =  ('name', 'country', 'satee_procince', 'city')
    search_fields = ('name','city','satee_procince')
    list_filter = ('satee_procince','country')
    ordering = ('name',)
    # fields = ('satee_procince','country')
    fieldsets = (
        (None, {
            'fields': ('name', 'country', 'address', )
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('satee_procince', 'city', 'website'),
        }),
    )


admin.site.register(Author)
admin.site.register(AuthorDetail)
admin.site.register(Book)

# 注册model类到admin的两种方式
# 方式一：使用register的方法
# admin.site.register(Publish, PublishAdmin)

