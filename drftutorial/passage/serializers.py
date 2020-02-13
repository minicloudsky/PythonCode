#!/usr/bin/env python
# coding=utf-8
from passage.models import Passage
from rest_framework import serializers


class PassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passage
        # filed = ('id', 'title', 'content', 'user', 'background_img',
        #           'like_count', 'post_time', 'is_draft')
        fields = '__all__'
