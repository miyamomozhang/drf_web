from django.http import JsonResponse, Http404
from .models import Article
from .serializers import ArticleListSerializer
from .permissions import IsAdminUserOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics

from rest_framework.permissions import IsAdminUser

# Create your views here.
# django的返回方式
"""
def article_list(request):
    articles = Article.objects.all()
    # 序列化
    serializer = ArticleListSerializer(articles, many=True)  # many=True 时传入的参数需要包含多个对
    return JsonResponse(serializer.data, safe=False)
"""

"""
# 不写请求方式的话，默认只支持GET请求
# FBV, django rest_framework
@api_view(["GET", "POST"])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
"""


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    # permission_classes = [IsAdminUser]
    permission_classes = [IsAdminUserOrReadOnly]


"""
# CBV，django rest_framework
class ArticleDetail(APIView):
    # 单个文章详情页
    def get_object(self, pk):
        # pk即prime key, 主键，唯一
        # 获取 pk 对应的文章对象
        try:
            return Article.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleListSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleListSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

"""
# 使用DRF 提供的 Mixin 类，实现增删改查
class ArticleDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = [IsAdminUserOrReadOnly]
