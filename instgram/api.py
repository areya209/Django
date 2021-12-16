from rest_framework import serializers
from .models import Post, Comment, Follow, User, Profile, Col
from rest_framework.authtoken.models import Token



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
        fields = ('username', 'password','email','first_name','last_name')
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class viewprofile(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields ='__all__'



class viewfollow(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'



class ADD(serializers.ModelSerializer):
    class Meta:
        model = Col
        fields = '__all__'