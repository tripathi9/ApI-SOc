from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from django.contrib.auth import update_session_auth_hash
from .models import*

class AccountSerializer(serializers.ModelSerializer):
    Password = serializers.CharField(write_only=True, required=True)


    class Meta:
        model = Account
        fields = (
            'UserId',
            'FirstName', 'LastName','Email', 'Password', 'PhoneNumber', 'Gender', 'Image')


    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)

class FeedSerializer(serializers.ModelSerializer):
        class Meta:
            model = Feeds
            fields = ('FeedId', 'FeedImage', 'Description', 'UserId', 'FeedTime')


class LikeSerializer(serializers.ModelSerializer):
        LikeCount = serializers.ReadOnlyField()

        class Meta:
            model = Likes
            fields = ( 'UserId', 'FeedId', 'LikeTime', 'LikeCount')

class FeedsSerializer(serializers.ModelSerializer):
        Id = serializers.ReadOnlyField()
        FirstName = serializers.ReadOnlyField()
        Image = serializers.ReadOnlyField()




        class Meta:
            model = Feeds

            fields = ('UserId', 'Id', 'FeedImage', 'FeedTime', 'Description','FirstName', 'Image')
