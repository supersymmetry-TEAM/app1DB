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
#    path("commentsfood/v1/", include("foodcomment.urls")),
#    path("board/v1/", include("board1.urls")),
#    path("commentsboard/v1/", include("boardcomment.urls")),
]
