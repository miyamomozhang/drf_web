from django.http import JsonResponse
from .models import Article
from .serializers import ArticleListSerializer


# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    # 序列化
    serializer = ArticleListSerializer(articles, many=True)  # many=True 时传入的参数需要包含多个对
    return JsonResponse(serializer.data, safe=False)