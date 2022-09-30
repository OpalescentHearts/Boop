from django.urls import path
from app import views
from app.views import bcca_view, bcca_team
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", bcca_view),
    path("<input>/", bcca_team, name="strawberry"),
]
