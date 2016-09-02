#!/usr/bin/python
# -*- coding:utf8 -*-

from django import forms



# 出版社的表单类，字段和model有点类似。
'''
# -----------------------------使用Form------------------------------
class PublishForm(forms.Form):
    name = forms.CharField(label='名称', error_messages={'required':'这个必须填写'})
    address = forms.CharField(label='地址', error_messages={'required':'这个必须填写'})
    city = forms.CharField(label='城市', error_messages={'required':'这个必须填写'})
    satee_procince = forms.CharField(label='省份', error_messages={'required':'这个必须填写'})
    country = forms.CharField(label='国家', error_messages={'required':'这个必须填写'})
    website = forms.URLField(label='网址', error_messages={'required':'这个必须填写'})
'''

# ------------------------------------使用ModelForm--------------------------------------------
from hello.models import Publish

from django.core.exceptions import ValidationError

'''
# 一、表单字段验证器
def validate_name(value): # 对应表单，加到哪个字段，哪个字段就传进来。
    try:
        Publish.objects.get(name = value)
        raise ValidationError('%s的信息已经存在' % value)
    except Publish.DoesNotExist:
        pass
'''

class PublishForm(forms.ModelForm):

    # 一、表单字段验证器
    # name = forms.CharField(label='名称', validators=[validate_name])

# 二、clean_filedname,验证字段,针对某个字段进行验证
#     def clean_name(self):
#         # clean_name是PublishForm的实例方法。
#         value = self.cleaned_data.get('name')
#         try:
#             Publish.objects.get(name = value)
#             raise ValidationError('%s的信息已经存在' % value)
#         except Publish.DoesNotExist:
#             pass
#         return value

    def clean(self):
        cleaned_data = super(PublishForm, self).clean()
        value = cleaned_data.get('name')
        try:
            Publish.objects.get(name = value)
            self._errors['name'] = self.error_class(['%s的信息已经存在' % value])
        except Publish.DoesNotExist:
            pass
        return cleaned_data

    class Meta:
        model = Publish
        exclude = ('id',)   # 注意逗号