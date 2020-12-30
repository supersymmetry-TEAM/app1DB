from django.urls import path
from api.views import ListFoodsView, KitoStandardView, NutView
from api.views import food_search, kito_search, nut_search, recomend_foods
app_name = "api"

urlpatterns = [
    path("search_nut/", nut_search),
    path("search_kito/", kito_search),
    path("search/", food_search),
    path("list/", ListFoodsView.as_view()),  
    path("kito/", KitoStandardView.as_view()),
    path("nut/", NutView.as_view()),
 path("recomend_foods/", recomend_foods), 
  ]

