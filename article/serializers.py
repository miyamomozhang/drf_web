# 新建serializers.py文件保存某应用的序列化器类


from rest_framework import serializers


class ArticleListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(allow_blank=True, max_length=200)
    body = serializers.CharField(allow_blank=True)
    create_time = serializers.DateTimeField()
    update_time = serializers.DateTimeField()
