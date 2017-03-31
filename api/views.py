from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import*
from .models import Account


class AuthRegister(APIView):
    """
    Register a new user.
    """
    serializer_class = AccountSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






@csrf_exempt
def post_feed(request):
    """
    List all code post, or create a new post.
    """
    if request.method == 'POST':
        # picture= MultiPartParser().parse('picture')
        data = JSONParser().parse(request)

        serializer = FeedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
def feed_likes (request):
    """
         likes on feeds
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        
        serializer = LikeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def login (request):
    params = JSONParser().parse(request)

    try:

      user = Account.objects.filter(Email=params["Email"]).last()
      chk = user.check_password(params["Password"])
      print(chk)
      if chk:
        print(chk)
        return JsonResponse({"UserId":user.UserId, "status":200,"Message":"Login Successfully"})
      else:
        return JsonResponse({"status":500,"Message":"Email & Password are not Correct"})
    except Account().DoesNotExist:
        return JsonResponse({"status":"500","Message":"email does not exist"})


@csrf_exempt
def get_all_feeds(request):
    """
    Retrieve, update or delete a post.
    """
    feed = Feeds.objects.all()




    serializer = FeedsSerializer(feed,many=True)
    return JsonResponse({"FeedList":serializer.data,"ResponseCode": "200","ResponseMessage":"Successfully"}, safe=False)
