# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html


import random


class UserAgentMiddleware(object):

    def __init__(self, user_agent_list):
        self.user_agent = user_agent_list

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        middleware = cls(crawler.settings.get('MY_USER_AGENT'))
        return middleware

    def process_request(self, request, spider):
        # 随机选择一个user-agent
        request.headers['user-agent'] = random.choice(self.user_agent)
