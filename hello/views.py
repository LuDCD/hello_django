#!/usr/bin/python
# -*- coding:utf8 -*-


from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpRequest

# Create your views here.


def hello(request):
	# print(request.method)		# GET
	# print(isinstance(request,HttpRequest))   # True
	# print(request.path)	# /hello/
	# print(request.POST.get('key'))
	# print(request.GET.get('name'))
	# print(request.POST.get('name'))


	user_list = User.objects.all()

	#
	print(user_list.query)

	# 方法一（推荐）
	# return render(request,'table.html',{'user_list':user_list})
	return render(request,'baseSon.html',{'user_list':user_list})

	# locals()方法
	# return render(request,'table.html',locals())
	# 方法二，自己构造HttpRequest对象
	# from django.template import loader
	# t = loader.get_template('table.html')
	# c = {'user_list': user_list}
	# return HttpResponse(t.render(c, request), content_type='text/html')

	# 方法三，使用render_to_response
	# from django.shortcuts import render_to_response
	# return render_to_response('table.html',{'user_list':user_list})


	# redirect方法
	# from django.shortcuts import redirect
	# return redirect('http://www.baidu.com')
'''
# --------------------------不使用Django Form,使用原生的html的表单。-------------------
from hello.models import *

def add_publish(request):
	if request.method == 'POST':
		# 如果为POST提交，去接收用户提交过来的数据
		name = request.POST['name']
		address = request.POST.get('address')
		city = request.POST.get('city')
		satee_procince = request.POST.get('satee_procince')
		country = request.POST.get('country')
		website = request.POST.get('website')
		# 写完的话，这里要加一个验证。
		# 通过create把传过来的数据写到model里面去（也就是写到数据库里面去）
		Publish.objects.create(
			name = name,
			address = address,
			city = city,
			satee_procince = satee_procince,
			country = country,
			website = website,
		)
		return HttpResponse("添加出版社成功")
	else:
		return render(request,'add_publish.html',locals())
'''

'''
# -------------------------使用Django Form的情况----------------
from hello.forms import PublishForm
from hello.models import Publish
def add_publish(request):
	if request.method == 'POST':
		publish_form = PublishForm(request.POST)	# 根据传过来的数据对表单初始化
		if publish_form.is_valid():
			Publish.objects.create(
				name = publish_form.cleaned_data['name'],
				address = publish_form.cleaned_data['address'],
				city = publish_form.cleaned_data['city'],
				satee_procince = publish_form.cleaned_data['satee_procince'],
				country = publish_form.cleaned_data['country'],
				website = publish_form.cleaned_data['website'],
			)
			return HttpResponse('添加出版社数据成功！')
	else:
		# 初始化一个表单对象
		publish_form = PublishForm()
	return render(request,'add_publish.html',locals())
'''

# -------------------------使用Django ModelForm的情况----------------
from hello.forms import PublishForm
from hello.models import Publish
def add_publish(request):
	if request.method == 'POST':
		publish_form = PublishForm(request.POST)	# 根据传过来的数据对表单初始化
		if publish_form.is_valid():
			publish_form.save()
			return HttpResponse('添加出版社数据成功！')
	else:
		# 初始化一个表单对象
		publish_form = PublishForm()
	return render(request,'add_publish.html',locals())




















