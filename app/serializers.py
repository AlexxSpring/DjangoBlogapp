from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # show username instead of user id
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = '__all__'