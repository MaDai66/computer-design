from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """订单项内联"""
    model = OrderItem
    extra = 0
    readonly_fields = ['subtotal']
    fields = [
        'item_type', 'name', 'image', 'price', 'quantity', 'subtotal', 'specs'
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """订单管理"""
    list_display = [
        'order_id', 'user', 'type', 'status', 'total_price',
        'contact_name', 'contact_phone', 'created_at'
    ]
    list_filter = ['status', 'type', 'created_at']
    search_fields = ['order_id', 'contact_name', 'contact_phone']
    readonly_fields = ['order_id', 'total_price', 'created_at', 'updated_at']
    inlines = [OrderItemInline]

    fieldsets = (
        ('基本信息', {
            'fields': ('order_id', 'user', 'type', 'status', 'total_price')
        }),
        ('联系人信息', {
            'fields': ('contact_name', 'contact_phone', 'contact_address')
        }),
        ('时间信息', {
            'fields': ('check_in', 'check_out', 'travel_date', 'guests', 'nights')
        }),
        ('支付信息', {
            'fields': ('payment_method', 'payment_time')
        }),
        ('其他', {
            'fields': ('notes', 'created_at', 'updated_at')
        }),
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """订单项管理"""
    list_display = [
        'id', 'order', 'item_type', 'name', 'price', 'quantity', 'subtotal'
    ]
    list_filter = ['item_type']
    search_fields = ['name', 'order__order_id']
    readonly_fields = ['subtotal']
