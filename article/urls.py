from django.urls import path
from . import views

urlpatterns = [
    # 所有文章
    # path("", views.article_list),
    path("", views.ArticleList.as_view()),
    # pk 对应的文章，name：给url一个名字，这样我们在别的地方用到的时候可以用name表示这个url
    # name的好处就是：如果我们的url需要改，我们只需要改这一个地方，其它地方用的是name不需要我们改
    # 我们只需要保证name的唯一
    path("<int:pk>/", views.ArticleDetail.as_view(), name="detail")
]
