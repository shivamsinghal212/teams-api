from django.urls import path
from . import views

urlpatterns = [
    path('member/', views.team_member),
    path('member/<int:pk>', views.team_member),

]
