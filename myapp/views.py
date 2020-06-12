from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import NewBlog
# Create your views here.
def index(request):
    return render(request,'myapp/index.html')

def read(request):
    blogs = Blog.objects.all()
    blog_list = Blog.objects.all()
    # 모든 Blog 글을 대상으로
    paginator = Paginator(blog_list, 3)
    # 블로그 객체 3개 한페이지로 자르기
    page = request.GET.get('page')
    # request된 페이지가 뭔지 알아낸다 (request페이지를 변수에 담는다)
    posts = paginator.get_page(page)
    # request된 페이지를 얻어온 뒤 return 해준다
    return render(request,'myapp/read.html',{'blogs':blogs,'posts':posts})

def create(request):
    if request.method =="POST":
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit = False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('myapp:read')
    else:
        form = NewBlog()
        return render(request,'myapp/create.html',{'form':form})