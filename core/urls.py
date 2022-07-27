from django.urls import path
from . import views


urlpatterns = [
    path('api/bills/', views.BillList.as_view()),
]
