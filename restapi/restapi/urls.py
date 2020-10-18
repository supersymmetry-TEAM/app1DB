from django.urls import include, path
from rest_framework import routers
from api import views
from django.contrib import admin


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("api/v1/foods/", include("api.urls")),
    path("admin/", admin.site.urls),
    path("usrs/v1/", include("users.urls")),
]