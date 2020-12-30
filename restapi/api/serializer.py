from rest_framework import serializers
from .models import FoodDatas, KitoStandard, NutData
from users.models import User
class RecomendSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodDatas
        fields = ("PRDLST_NM",)

class FoodSerializer(serializers.ModelSerializer):

    #user = TinyUserSerializer()  if there is user field... we can analize user field.. if user class hav serializer
    is_fav = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    class Meta:
        model = FoodDatas
        fields = '__all__'
    def get_likes(self, obj):
        likes = User.objects.filter(favs__in=[obj]).count()
        return likes
    
    def get_is_fav(self, obj):
        request = self.context.get("request")
        if request:
            user = User.objects.get(pk=request.query_params.get('id'))
            return obj in user.favs.all()
        return False

class KitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitoStandard
        fields = '__all__'
        


class NutDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutData
        fields = '__all__'
