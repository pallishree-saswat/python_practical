from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import(
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView
)

from api import serializers, models
import json

# Create your views here.


@api_view()
def getArticles(request):
    articles = models.Articles.objects.all()
    response = serializers.ArticleSerializer(articles, many=True)
    return Response(response.data)


@api_view(['POST'])
def createArticle(request):
    print(request.body)
    body = json.loads(request.body)
    response = serializers.ArticleSerializer(data=body)

    if response.is_valid():
        newdata = response.save()
        response = serializers.ArticleSerializer(newdata)
        return Response(response.data)
    return Response(response.errors)


# class ArticleListView(ListAPIView): only get all data cant post data to db
class ArticleListView( ListCreateAPIView): #can get data with get request  and post data if we make post request with body
    queryset = models.Articles.objects.all()
    serializer_class = serializers.ArticleSerializer


# class ArticleDetailview(RetrieveAPIView): only we can get single api details but cant update with patch request
class ArticleDetailview(RetrieveUpdateAPIView):   #if we do get request with parameter then it will give single data and if we do patch request it will update those fileds
    queryset = models.Articles.objects.all()
    serializer_class = serializers.ArticleSerializer


""" 

class ArticlesListView(ListCreateAPIView):
  serializer_class = serializers.ArticleSerializer

  def get_queryset(self):
    query = {}
    for key, value in self.request.GET.items():
      query["{}__icontains".format(key)] = value

    return models.Article.objects.filter(**query)


    localhost:8000/api/articles/?title=article

 """