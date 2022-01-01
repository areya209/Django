from rest_framework import serializers
from .models import Post, Comment, Follow, User, Profile, Col, Likes
from rest_framework.authtoken.models import Token


# from django_filters import FilterSet


class Commentadd(serializers.ModelSerializer):
    username = serializers.CharField(source='profile.username')

    class Meta:
        model = Comment
        fields = '__all__'


class USerview(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class POSRSIL(serializers.ModelSerializer):
    comment = Commentadd(read_only=True, many=True)
    username = serializers.CharField(source='profile.username')

    class Meta:
        model = Post
        fields = '__all__'


class viewprofile(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'bio', 'profile_pic', 'user')

        def update(self, instance, validated_data):
            mode_of_payment = validated_data.pop('user')
            instance.mode_of_payment_user = mode_of_payment.user
            return instance


class viewfollow(serializers.ModelSerializer):
    username_from = serializers.CharField(source='user_from.username')
    username_to = serializers.CharField(source='user_to.username')

    class Meta:
        model = Follow
        fields = '__all__'


class ADD(serializers.ModelSerializer):
    class Meta:
        model = Col
        fields = '__all__'


class ProfileSer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


#  Like
class viewlike(serializers.ModelSerializer):
    username = serializers.CharField(source='user_like.username')

    class Meta:
        model = Likes
        fields = '__all__'


# Update
# class StatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Status
#
#
# class ModelIssueSerializer(serializers.ModelSerializer):
#     status = StatusSerializer()
#
#     # ...
#     def update(self, instance, validated_data):
#         status = validated_data.pop('status')
#         instance.status_id = status.id
#         # ... plus any other fields you may want to update
#         return instance


# Reset Password Of User
class ChangePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('password', 'new_password', 'confirm_password')

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"new_password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['new_password'])
        instance.save()

        return instance
