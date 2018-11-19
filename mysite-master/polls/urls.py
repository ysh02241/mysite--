from django.contrib import admin
from django.urls import path

from polls.views import index, datail, datail2, datail3, vote

urlpatterns = [
    path('', index),
    path('<int:question_id>', datail,name='detail'),
    path('<int:num1>/<int:num2>', datail2),
    path('<int:num1>a', datail3),
    path('<int:question_id>/vote', vote),
]
