#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-12-28 16:59
#@Author: ley
#@Site : 
#@File : testdb.py
#@Software : PyCharm

from django.http import  HttpResponse
from Testmodle1.models import Test

#添加数据
'''def testdb(request):
    test1=Test(name='jack')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")'''

#获取数据
def testdb(request):
    #初始化
    response=""
    response1=""
    # 通过object 这个模型管理器的all()获取所有数据行,相当于select * from
    list = Test.objects.all()

    for var in list:
        response1 += var.name + " "
    response=response1
    return HttpResponse("<p>" + response + "</p>")

def updatedb(request):
    test1=Test.objects.get(id=2)
    test1.name='baidu'
    test1.save()
    return HttpResponse("<p>修改成功</p>")
#filter相当于SQL中的where ，可以设置条件过滤结果
#response2=Test.objects.filter(id=1)

#获取单个对象
#response3=Test.objects.get(id=1)

#限制返回的数据，相当于SQL中的OFFSET 0 lIMIT 2
#Test.objects.order_by('name')[0:2]

#数据排序
#Test.objects.order_by("id")

#上面的方法可以连锁使用

#Test.objects.filter(name="rubby").order_by("id")

#输出所有数据












