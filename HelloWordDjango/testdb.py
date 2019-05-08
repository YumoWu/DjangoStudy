# -*- coding: utf-8 -*-
from django.http import HttpResponse
from TestModel.models import Test



# 数据库操作
def testdb(request):
    # test1 = Test(name='runoob')
    # test1.save()
    # return HttpResponse("<p>数据添加成功！</p>")
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()

    # filter相当于SQL中的WHERE， 可设置条件过滤结果
    response2 = Test.objects.filter(id=1)

    # 获取单个对象
    response3 = Test.objects.get(id=1)

    