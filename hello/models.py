#!/usr/bin/python
# -*- coding:utf8 -*-

from django.db import models

# Create your models here.

# 出版商模型
class Publish(models.Model):
    name = models.CharField(max_length=30, verbose_name='名称')
    address = models.CharField('地址', max_length=50)     # 在第一个参数设置
    city = models.CharField('城市', max_length=60)
    satee_procince = models.CharField('省份', max_length=30)
    country = models.CharField('国家', max_length=50)
    website = models.URLField(verbose_name = '网址')

    class Meta:
        verbose_name = '出版商'
        verbose_name_plural = '出版商'
        # ordering = ['排序字段']

    def __str__(self):
        return self.name

    # class Meat:
    #     verbose_name = '名称'
    #     verbose_name_plural = '名称复数形式'
    #     ordering = ['排序字段']



# 作者模型
class Author(models.Model):
    name = models.CharField('姓名', max_length=30)

    class Meta:
        verbose_name = '作者姓名'
        verbose_name_plural = '作者姓名'

    def __str__(self):
        return self.name


# 详细作者模型
class AuthorDetail(models.Model):
    sex = models.BooleanField('性别', max_length=1,choices=((0, '男'),(1, '女'),))
    email = models.EmailField()
    address = models.CharField('地址', max_length=50)
    birthday = models.DateField('出生日期')
    author = models.OneToOneField(Author, verbose_name = '姓名')   # 一对一

    class Meta:
        verbose_name = '作者详情'
        verbose_name_plural = '作者详情'
        # ordering = ['排序字段']

    def __str__(self):      # 新建的对象的名字
        return self.author.name

# 书籍模型
class Book(models.Model):
    title = models.CharField('书名', max_length=100)
    author = models.ManyToManyField(Author, verbose_name = '作者')     # 多对多
    publisher = models.ForeignKey(Publish, verbose_name = '出版商')    # 一对多（外键）
    publication_date = models.DateField('出版日期')
    price = models.DecimalField(max_digits=5,decimal_places=2,default=10)        # 5个数字，其中2个是小数。
    # 价格可以是999.99-000.00

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = '书籍'
        # ordering = ['排序字段']

    def __str__(self):
        return self.title
