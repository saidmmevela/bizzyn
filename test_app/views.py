# from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from .models import TestModel,UserModel
from .serializers import SimpleObjectSerializer,UserSerializer
from django.contrib.auth import authenticate, login
# def sample(request):
# Create your views here.
    # method = request.method.lower()
    # if method == "get":
    #     return JsonResponse({"data": [1,2,3,4,5]})
    # elif  method == "post":
    #     return JsonResponse({"data": "Added data successfully"})
    # elif  method == "put":
    #     return JsonResponse({"data": "Updated data successfully"})
    # return JsonResponse({"method": "method not allowed"})

class Sample(APIView):
    def post(self, request):
        serializer = SimpleObjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # new_test_content = TestModel.objects.create(
        #     name=request.data["name"],
        #     description=request.data["description"],
        #     phone_number=request.data["phone_number"],
        #     is_live=request.data["is_live"],
        #     amount=request.data["amount"]
        # )
        serializer.save()
        return JsonResponse({"data": serializer.data})
        # return JsonResponse({"data": SimpleObjectSerializer(new_test_content).data})
        # return JsonResponse({"data": request.data})

    def get(self, request):
        content = TestModel.objects.all().values()
        return JsonResponse({"data": SimpleObjectSerializer(content, many=True).data})
    
    def put(self, request, *args, **kwargs):
        model_id = kwargs.get("id", None)
        if not model_id:
            return JsonResponse({"error": "method /PUT/ not allowed" })

        try:
            instance = TestModel.objects.get(id=model_id)
        except:
            return JsonResponse({"error": "Object does not exist" })

        serializer = SimpleObjectSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"data": serializer.data})

class UserGeneric(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        # user = UserModel.objects.get(username=username, password=password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # serializer.is_valid(raise_exception=True)
            user1 = UserModel.objects.get(username=username, password=password)
            return JsonResponse({"data": UserSerializer(user1).data})
        
        return JsonResponse({"data": "invalid credential"})

class SampleGeneric(generics.ListCreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = SimpleObjectSerializer

class SampleGenericUpdate(generics.UpdateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = SimpleObjectSerializer
    lookup_field = "id"

class SampleViewSet(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = SimpleObjectSerializer