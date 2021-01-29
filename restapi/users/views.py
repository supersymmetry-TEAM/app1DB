import jwt
from django.conf import settings
from django.contrib.auth import authenticate


from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.models import FoodDatas
from api.serializer import FoodSerializer

from .permission import IsSelf 
from .models import User
from .serializer import UserSerializer, UserInfoSerializer



class UsersViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == "list":
            permission_classes = [IsSelf]
            # permission_classes = [IsAdminUser]
        elif (
            self.action == "create"
            or self.action == "retrieve"
            or self.action == "favs"
        ):            
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsSelf]

        return [permission() for permission in permission_classes]
  

    @action(detail=False, methods=["post"])
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if user is not None:
            encoded_jwt = jwt.encode(
                {"pk": user.pk}, settings.SECRET_KEY, algorithm="HS256"
            )
            return Response(data={"token": encoded_jwt, "id": user.pk})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    @action(detail=True, methods=["put","get"])
    def info(self, request,pk):
        # username = request.data.get("username")
        # password = request.data.get("first_name")
        # password = request.data.get("last_name")
        # password = request.data.get("email")
        serializer = UserInfoSerializer(request.user, 
        data=request.data, partial=True,
        context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    @action(detail=True)
    def favs(self, request, pk):
        user = self.get_object()
        serializer = FoodSerializer(user.favs.all(), many=True, context={"request": request}).data
        return Response(serializer)
    
    @favs.mapping.put
    def toggle_favs(self, request, pk):
        pk = request.data.get("pk", None)
        user = self.get_object()
        if pk is not None:
            try:
                room = FoodDatas.objects.get(pk=pk)
                if room in user.favs.all():
                    user.favs.remove(room)
                else:
                    user.favs.add(room)
                return Response()
            except FoodDatas.DoesNotExist:
                pass
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=["post"])
    def change_password(self, request):
        newpassword = request.data.get("newpassword")
        userid = int(request.data.get("userid"))
        try:
            u = User.objects.get(pk=userid)
            u.set_password(newpassword)
            u.save()
            return Response(status=status.HTTP_200_OK)
        except ValueError:
            return Response({"messege":"something wrong"})


# class FavsView(APIView):

#     permission_classes = [IsAuthenticated]
#     def get(self, request):
#         user = request.user
#         serializer = FoodSerializer(user.favs.all(), many=True).data
#         return Response(serializer)
#     def put(self, request):
#         pk = request.data.get("pk", None)
#         user = request.user
#         if pk is not None:
#             try:
#                 room = FoodDatas.objects.get(pk=pk)
#                 if room in user.favs.all():
#                     user.favs.remove(room)
#                 else:
#                     user.favs.add(room)
#                 return Response()
#             except FoodDatas.DoesNotExist:
#                 pass
#         return Response(status=status.HTTP_400_BAD_REQUEST)



