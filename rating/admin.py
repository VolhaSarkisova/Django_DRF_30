from django.contrib import admin
from rating.models import Rating
# Register your models here.
# Register your models here.
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('value', 'product')
    search_fields = ('value', )
    list_filter = ('value', )
