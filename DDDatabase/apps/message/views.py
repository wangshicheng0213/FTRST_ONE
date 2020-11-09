# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from .models import DDKBGene,UserMessage,Post

# 从数据库中查询数据
def get_value(names):
    # all_messages = UserMessage.objects.all()
    all_messages = UserMessage.objects.filter(name=names)
    # for message in all_messages:
    #     print(message.name)
    return all_messages
#get_value('wangshicheng')
# 数据表的存储
# def  getform(request):
#
#     user_message = UserMessage()
#     user_message.name = "bobby2"
#     user_message.message = "helloword"
#     user_message.address = "shansong"
#     user_message.email = "2@2.com"
#     user_message.object_id = "hello"
#     user_message.save()
#
#     return render(request,'message_form.html')


#取到从页面当中传过来的值,完成了一个表单的提交
# def  getform(request):
#     if request.method == "POST":
#         # get取字典里面值的方法，如果取不到，那么默认值为空
#         name = request.POST.get('name','')
#         message = request.POST.get('message', '')
#         address = request.POST.get('address', '')
#         email = request.POST.get('email', '')
#         user_message = UserMessage()
#         user_message.name = name
#         user_message.message = message
#         user_message.address = address
#         user_message.email = email
#         user_message.object_id = "hello4"
#         user_message.save()
#     return render(request,'message_form.html')


# 将数据库的数据显示到我们的页面上
def  getform(request):
    message = None
    all_messages = UserMessage.objects.filter(name = "wangshicheng")
    # for message in all_messages:
    #     print(message.name)
    # 这里的queryset 是一个数组
    if all_messages:
        message = all_messages[0]
    return render(request,'message_form.html',{"my_message":message})





def  getHome(request):

    return render(request, 'Home.html')
def  getPPINetwork(request):

    return render(request, 'PPINetwork.html')
def  getCoExAnalysis(request):

    return render(request, 'CoExAnalysis.html')
def  getExPaAnalysis(request):

    return render(request, 'ExPaAnalysis.html')
def  getDownload(request):

    return render(request, 'Download.html')
def  getManual(request):

    return render(request, 'Manual.html')
def  getSearchGene(request):
    return render(request, 'SearchGene.html')

def search(request):
    # 声明两个变量
    # 从页面上得到
    q = request.GET.get('q')
    error_msg = ''

    # 如果没有得到这个q
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'results.html', {'error_msg': error_msg})

    #post_list = Post.objects.filter(title__icontains=q)
    # 这里添加一个取数据的函数
    post_list = get_value(q)
    print(post_list)
    #post = q
    # 将post传入到前端的页面
    return render(request, 'result.html', {'error_msg': error_msg,
                                               'post_list': post_list})

