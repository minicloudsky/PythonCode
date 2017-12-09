# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field


class UserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    allow_message = Field()
    answer_count = Field()
    articles_count= Field()
    employments = Field()
    avatar_url= Field()
    avatar_url_template= Field()
    badge = Field()
    follower_count  = Field()
    gender = Field()
    headline  = Field()
    id  = Field()
    is_advertiser = Field()
    is_blocking = Field()
    is_followed = Field()
    is_following = Field()
    is_org = Field()
    name = Field()
    type = Field()
    url = Field()
    url_token = Field()
    user_type = Field()
