from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from orderlist.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    def url_tg(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.contact)

    def get_image(self, obj):
        html_images = f'''<img src={obj.image.url} height="100">'''
        return mark_safe(html_images)

    get_image.short_description = 'Фотография'
    url_tg.short_description = 'Ссылка на пользователя, оформившего заказ'
    list_display = ('id', 'date_create')
    fields = ('get_image', 'size', 'url_tg')
    readonly_fields = ('get_image', 'url_tg')