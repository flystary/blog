#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "版权所有@源码商城：https://shop530346312.taobao.com/?spm=a1z10.1-c.0.0.1c1f6daeeNP5VM"
__date__ = "2019/05/08 16:39"

# 该文件是一个简单的前端过滤器，在前端页面需要引入后，即可使用自定义的函数，对前端的数据进行过滤
# django的这个功能，对于js不熟的小伙伴，是个福音

from django import template

register = template.Library()  # 获取到Django模板所有tags和filter的library，以便我们写入一个新的方法


@register.filter(name='value_get')  # 过滤器在模板中使用时的name
def value_get(banner_arts, value):  # 自定义方法
    """
    获取指定轮播文章的指定的值
    banner_arts：轮播文章对象集合，需要同前端页面中的名称保持一致，默认传入
    value_get：前端传入的参数，第一位是文章的id，第二位是需要返回的属性字段
    """

    # 文章为空时
    if not banner_arts:
        return

    value = str(value).split(',')
    pk = int(value[0])
    val = value[1]

    if val == 'img':
        return banner_arts[pk - 1].img
    elif val == 'cat_id':
        return banner_arts[pk-1].categorie_id
    elif val == 'categorie':
        return banner_arts[pk - 1].categorie
    elif val == 'art_id':
        return banner_arts[pk - 1].id
    elif val == 'title':
        return banner_arts[pk - 1].title

