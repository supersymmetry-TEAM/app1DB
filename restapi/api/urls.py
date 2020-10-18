from django.urls import path
from api.views import ListFoodsView,KitoStandardView
from api.views import food_search,kito_search
app_name = "api"

urlpatterns = [
    path("search_kito/", kito_search),
    path("search/", food_search),
    path("list/", ListFoodsView.as_view()),  
    path("kito/", KitoStandardView.as_view()),  
]

