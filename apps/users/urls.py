from django.urls import path

from settings import SuffixRouter

from . import views


urlpatterns = [
    path(f"{SuffixRouter.USERS}/<str:username>/", views.get_user_by_name, ),
]



