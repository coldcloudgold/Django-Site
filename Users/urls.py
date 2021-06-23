from django.urls import path
from .views import *

urlpatterns = [
    path(
        "password/change/",
        password_change,
        name="custom_change_password",
    ),
    path(
        "password/change/done",
        password_change_done,
        name="custom_change_password_done",
    ),
]
