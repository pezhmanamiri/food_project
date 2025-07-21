from django import template
import jdatetime

register = template.Library()

@register.filter
def persian_weekday(date_obj):
    weekdays = ['دوشنبه', 'سه‌شنبه', 'چهارشنبه', 'پنج‌شنبه', 'جمعه', 'شنبه', 'یک‌شنبه']
    # تبدیل هفته میلادی (Mon=0) به شنبه=0
    weekday_index = (date_obj.weekday() + 0) % 7
    return weekdays[weekday_index]

@register.filter
def to_jalali(date_obj):
    j_date = jdatetime.date.fromgregorian(date=date_obj)
    return j_date.strftime('%Y/%m/%d')



@register.filter
def dict_get(d, key):
    return d.get(key)




@register.filter
def dict_get(d, key):
    return d.get(key)
