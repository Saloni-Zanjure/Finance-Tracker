from django.contrib import admin
from .models import Expense, Category
# Register your models here.


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['owner', 'amount','description', 'date', 'category']
    search_fields = ['owner', 'category', 'date','description']
    list_per_page = 5


admin.site.register(Expense,ExpenseAdmin)
admin.site.register(Category)
