from django.urls import path

# importing views from views..py
from .views import GeeksCreate, GeeksList, GeeksDetailView, GeeksUpdateView, GeeksDeleteView
urlpatterns = [
	path('create/', GeeksCreate.as_view()),
    path('list/', GeeksList.as_view()),
    path('list/<pk>/', GeeksDetailView.as_view()),
    path('list/<pk>/update/', GeeksUpdateView.as_view()),
    path('list/<pk>/delete/', GeeksDeleteView.as_view()),
]

