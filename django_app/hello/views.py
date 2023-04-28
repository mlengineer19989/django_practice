from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
import typing as tp
from .forms import FriendForm, FindForm
from .models import Friend

class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend

# class HelloView(TemplateView):
#     def __init__(self, **kwargs: tp.Any) -> None:
#         super().__init__(**kwargs)
#         self.params:tp.Dict[str, tp.Any] = {
#             "title":"Hello",
#             "message":"your data:",
#             "form":HelloForm(),
#         }

#     def get(self, request:HttpResponse) -> HttpResponse:
#         return render(request, "hello/index.html", self.params)
    
#     def post(self, request:HttpResponse) -> HttpResponse:
#         msg = "あなたは、<b>" + request.POST["name"] + \
#             " (" + request.POST["age"] + \
#             ") </b>さんです。<br>メールアドレスは <b>" + request.POST["mail"] + \
#             "</b> ですね。"
        
#         self.params["message"] = msg
#         self.params["form"] = HelloForm(request.POST)
#         return render(request, "hello/index.html", self.params)

def index(request:HttpResponse) -> HttpResponse:
    data = Friend.objects.all()
    params:tp.Dict[str, any] = {
        'title':'Hello',
        "data":data,
    }

    return render(request, "hello/index.html", params)

#create model
def create(request:HttpResponse):
    if (request.method == "POST"):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to="/hello")
    params:tp.Dict[str, any] = {
        'title':'Hello',
        "form":FriendForm(),
    }
    
    return render(request, "hello/create.html", params)

def edit(request:HttpResponse, num:int):
    obj = Friend.objects.get(id=num)
    if (request.method == "POST"):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params:tp.Dict[str, any] = {
        'title':'Hello',
        'id':num,
        'form':FriendForm(instance=obj),
    }
    return render(request, 'hello/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params:tp.Dict[str, any] = {
        'title':'Hello',
        'id':num,
        'obj':friend,
    }
    return render(request, 'hello/delete.html', params)

def find(request:HttpResponse):
    if (request.method == "POST"):
        form = FindForm(request.POST)
        find = request.POST['find']
        data = Friend.objects.filter(name__contains=find)
        msg = 'Result: ' + str(data.count())
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params:tp.Dict[str, any] = {
        'title':'Hello',
        'message':msg, 
        "form":form,
        'data':data,
    }
    
    return render(request, "hello/find.html", params)

# def next(request:HttpResponse) -> HttpResponse:
#     params:tp.Dict[str, str] = {
#         'title':'Hello/Next',
#         'msg':'これは、サンプルで作ったページです。',
#         'goto':'index',
#     }
#     return render(request, "hello/index.html", params)

# def form(request:HttpResponse) -> HttpResponse:
#     msg:str = request.POST["msg"]
#     params:tp.Dict[str, str] = {
#         "title":"hello/Form",
#         "msg":"こんにちは、" + msg + "さん。",
#     }
#     return render(request, "hello/index.html", params)
