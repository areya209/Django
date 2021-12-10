from rest_framework import serializers
from .models import Post,Comment,Follow,User,Profile

class POSRSIL(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields ='__all__'
class Commentadd(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields ='__all__'


class USerview(serializers.ModelSerializer):

    class Meta:
        model = User
        fields ='__all__'


class viewprofile(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields ='__all__'


class viewfollow(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'
