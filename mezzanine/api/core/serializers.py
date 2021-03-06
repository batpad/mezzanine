from django.contrib.sites.models import Site
from django.contrib.auth.models import User

from rest_framework import serializers

from mezzanine.pages.models import Page


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site

