from rest_framework import serializers
from .models import FoodDatas, KitoStandard
from users.models import User

class FoodSerializer(serializers.ModelSerializer):

    #user = TinyUserSerializer()  if there is user field... we can analize user field.. if user class hav serializer
    is_fav = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    class Meta:
        model = FoodDatas
        exclude = ()
    def get_likes(self, obj):
        likes = User.objects.filter(favs__in=[obj]).count()
        return likes
    
    def get_is_fav(self, obj):
        request = self.context.get("request")
        if request:
            user = request.user
            if user.is_authenticated:
                return obj in user.favs.all()
        return False

class KitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitoStandard
        exclude = ()
        



