from django.urls import path # type: ignore
from .import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns =[ 
    
    path('',views.index, name="expenses"),
    path('add-expenses',views.add_expense, name='add-expense'),
    path('expense-edit/<int:id>',views.expense_edit, name='expenses-edit'),
    path('expense-delete/<int:id>',views.delete_expense, name='expenses-delete'),
    path('search-expenses',views.search_expenses, name='search-expenses'),
    path('expense_category_summary', views.expense_category_summary,
         name="expense_category_summary"),
    path('stats', views.stats_view,
         name="stats"),
    path('export_csv', views.export_csv, name='export_csv'),
    
]