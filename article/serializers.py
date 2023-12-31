# 新建serializers.py文件保存某应用的序列化器类


from rest_framework import serializers

# 序列化器 和 我们之前的 Model 很像，代码重复，ModelSerializer简化
from .models import Article

"""
class ArticleListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(allow_blank=True, max_length=200)
    body = serializers.CharField(allow_blank=True)
    create_time = serializers.DateTimeField()
    update_time = serializers.DateTimeField()
"""


# 序列化器 和 我们之前的 Model 很像，代码重复，ModelSerializer简化
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        # fields = '__all__'代表要使用所有的字段

        # 只使用一部分字段，就用下面的方式
        # fields = [
        #     "id",
        #     "title",
        #     "create_time",
        #     # "update_time",
        # ]
