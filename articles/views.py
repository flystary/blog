#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 常规模块的引入分为三部分，依次为：
# Python内置模块（如json、datetime）、第三方模块（如Django）、自己写的模块

import json

from django.shortcuts import render, HttpResponse  # render方法实现后台页面渲染，HttpResponse方法实现后端通过HTTP协议同前端通信
from django.http import JsonResponse  # JsonResponse方法实现后端向前端传输json格式的数据
from django.views.generic import View  # 使用Django的view视图类
from django.shortcuts import get_object_or_404  # get_object_or_404方法可以在未找到指定内容时，直接抛出404异常
from django.db.models import Q  # 实现复杂查询，常用于全局搜索功能
from pure_pagination import Paginator, PageNotAnInteger  # 实现分页功能

from .models import Info, Categories, Tags, Articles, GetMessage
from .forms import GetMessageForm


# TODO: 已完成try的使用，接下来要做搜索问题的处理

class Index(View):
    """首页视图"""

    def get(self, request):
        try:
            # 以下部分可以定义为全局变量，感兴趣的同学可以尝试
            info = Info.objects.all().order_by('id')
            if info: info = info[0]
            categories = Categories.objects.all().order_by('id')
            articles = Articles.objects.all()

            # 首页/footer 轮播文章
            banner_arts = articles.filter(is_index=1)
            if len(banner_arts) >= 6:  # 首页轮播默认选择6篇文章
                banner_arts = banner_arts[:6]
            elif banner_arts:  # 不足6篇文章，则使用最后一篇文章凑数
                banner_arts = list(banner_arts)
                for i in range(6 - len(banner_arts)):
                    banner_arts.append(banner_arts[-1])

            # Popular Post  按阅读数排序，取前4个
            popular_articles = articles.order_by('-click_nums')
            if len(popular_articles) > 4: popular_articles = popular_articles[:4]

            # 首页文章列表，按id排序，分页，部署时建议改为按更新时间进行排序
            list_articles = articles.order_by('id')
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(list_articles, 4, request=request)
            list_articles = p.page(page)

            # 传到前端的参数
            context = {
                'info': info,
                'categories': categories,
                'banner_arts': banner_arts,
                'list_articles': list_articles,
                'popular_articles': popular_articles,

            }
            return render(request, 'index.html', context)
        except BaseException as e:
            return render(request, 'index.html', {})


class CategoriesView(View):
    """博客文章列表"""

    def get(self, request, pk):
        try:
            # 以下部分可以定义为全局变量，感兴趣的同学可以尝试
            info = Info.objects.all().order_by('id')
            if info: info = info[0]
            categories = Categories.objects.all().order_by('id')
            articles = Articles.objects.all()

            # 首页/footer 轮播文章
            banner_arts = articles.filter(is_index=1)
            if len(banner_arts) >= 6:  # 首页轮播默认选择6篇文章
                banner_arts = banner_arts[:6]
            else:  # 不足6篇文章，则使用最后一篇文章凑数
                banner_arts = list(banner_arts)
                for i in range(6 - len(banner_arts)):
                    banner_arts.append(banner_arts[-1])

            # Popular Post  按阅读数排序，取前4个
            popular_articles = articles.order_by('-click_nums')
            if len(popular_articles) > 4: popular_articles = popular_articles[:4]

            # 文章分类列表，按id排序，分页，部署时建议改为按更新时间进行排序
            list_articles = articles.filter(categorie=pk).order_by('id')
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(list_articles, 4, request=request)
            list_articles = p.page(page)

            # 传到前端的参数
            context = {
                'info': info,
                'categories': categories,
                'banner_arts': banner_arts,
                'list_articles': list_articles,
                'popular_articles': popular_articles,

            }
            return render(request, 'categories.html', context)
        except BaseException as e:
            return render(request, 'categories.html', {})


class ArticlesView(View):
    """文章详情页"""

    def get(self, request, pk):
        try:
            # 以下部分可以定义为全局变量，感兴趣的同学可以尝试
            info = Info.objects.all().order_by('id')
            if info: info = info[0]
            categories = Categories.objects.all().order_by('id')
            articles = Articles.objects.all()

            # 首页/footer 轮播文章
            banner_arts = articles.filter(is_index=1)
            if len(banner_arts) >= 6:  # 首页轮播默认选择6篇文章
                banner_arts = banner_arts[:6]
            else:  # 不足6篇文章，则使用最后一篇文章凑数
                banner_arts = list(banner_arts)
                for i in range(6 - len(banner_arts)):
                    banner_arts.append(banner_arts[-1])

            # Popular Post  按阅读数排序，取前4个
            popular_articles = articles.order_by('-click_nums')
            if len(popular_articles) > 4: popular_articles = popular_articles[:4]

            # 传到前端的参数
            article = get_object_or_404(articles, pk=pk)
            tags = Tags.objects.filter(articles=article)
            # 增加阅读数
            article.viewed()
            context = {
                'info': info,
                'categories': categories,
                'banner_arts': banner_arts,
                'popular_articles': popular_articles,
                'article': article,
                'tags': tags,

            }
            return render(request, 'article.html', context)
        except BaseException as e:
            return render(request, 'article.html', {})


class ContactView(View):
    """联系页"""

    def get(self, request):
        try:
            # 以下部分可以定义为全局变量，感兴趣的同学可以尝试
            info = Info.objects.all().order_by('id')
            if info: info = info[0]
            categories = Categories.objects.all().order_by('id')
            articles = Articles.objects.all()

            # 首页/footer 轮播文章
            banner_arts = articles.filter(is_index=1)
            if len(banner_arts) >= 6:  # 首页轮播默认选择6篇文章
                banner_arts = banner_arts[:6]
            else:  # 不足6篇文章，则使用最后一篇文章凑数
                banner_arts = list(banner_arts)
                for i in range(6 - len(banner_arts)):
                    banner_arts.append(banner_arts[-1])

            # Popular Post  按阅读数排序，取前4个
            popular_articles = articles.order_by('-click_nums')
            if len(popular_articles) > 4: popular_articles = popular_articles[:4]

            address_city = info.area.name
            if address_city in ['北京市', '天津市', '上海市', '重庆市']:
                info.address = str(info.area.province.name) + '市辖区' + str(info.address)
            else:
                info.address = str(info.area.province.name) + str(info.area.name) + str(info.address)

            # 传到前端的参数
            context = {
                'info': info,
                'categories': categories,
                'banner_arts': banner_arts,
                'address': json.dumps(info.address),
                'city': json.dumps(info.area.name),
            }
            return render(request, 'contact.html', context)
        except BaseException as e:
            print(e)
            return render(request, 'contact.html', {})


class MsgView(View):
    """留言处理"""

    def post(self, request):
        msg = GetMessage()
        msg_form = GetMessageForm(request.POST)
        res = dict()
        if msg_form.is_valid():  # 通过验证
            msg.name = request.POST.get('name', '')
            msg.email = request.POST.get('email', '')
            msg.subject = request.POST.get('subject', '')
            msg.message = request.POST.get('message', '')
            msg.save()
            res['status'] = 'success'
        else:
            res['status'] = 'fail'
            for key, error in msg_form.errors.items():
                res['msg'] = error
                break  # 只显示第一个错误
        return HttpResponse(json.dumps(res), content_type='application/json')


class SearchView(View):
    """搜索视图"""

    def get(self, request):
        try:
            # 以下部分可以定义为全局变量，感兴趣的同学可以尝试
            info = Info.objects.all().order_by('id')
            if info: info = info[0]
            categories = Categories.objects.all().order_by('id')
            articles = Articles.objects.all()

            # 首页/footer 轮播文章
            banner_arts = articles.filter(is_index=1)
            if len(banner_arts) >= 6:  # 首页轮播默认选择6篇文章
                banner_arts = banner_arts[:6]
            else:  # 不足6篇文章，则使用最后一篇文章凑数
                banner_arts = list(banner_arts)
                for i in range(6 - len(banner_arts)):
                    banner_arts.append(banner_arts[-1])

            # Popular Post  按阅读数排序，取前4个
            popular_articles = articles.order_by('-click_nums')
            if len(popular_articles) > 4: popular_articles = popular_articles[:4]

            keyword = request.GET.get('keyword', '')
            # 从标题、摘要进行搜索结果
            list_articles = articles.filter(Q(title__icontains=keyword) | Q(info__icontains=keyword))
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(list_articles, 4, request=request)
            list_articles = p.page(page)

            # 传到前端的参数
            context = {
                'info': info,
                'categories': categories,
                'banner_arts': banner_arts,
                'list_articles': list_articles,
                'popular_articles': popular_articles,

            }
            return render(request, 'categories.html', context)
        except BaseException as e:
            return render(request, 'categories.html', {})


class AddFavView(View):
    """点赞处理"""

    def get(self, request, pk):
        try:
            if pk:
                article = get_object_or_404(Articles, pk=pk)
                # 增加点赞数
                article.addfav()
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'failed'})

        except BaseException as e:
            return JsonResponse({'status': 'failed'})
