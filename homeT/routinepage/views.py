from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    posts = Routine.objects.all().order_by('-id')
    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    return render(request,'home.html',{'page_posts' : page_posts})

def new(request):
    return render(request,'postnew.html')

def postcreate(request):
    post=Routine()
    post.title=request.POST['title']
    post.url1=request.POST['url1']
    post.part1=request.POST['part1']
    post.url2=request.POST['url2']
    post.part2=request.POST['part2']
    post.save()
    return redirect('routinepage:home')

def detail(request, post_id):
    onepost = get_object_or_404(Routine, pk=post_id)
    comments = onepost.comment_set.all()
    return render(request, 'detail.html', {'onepost' : onepost, 'comments' : comments})

def postedit(request, post_id):
    onepost = get_object_or_404(Routine, pk=post_id)
    return render(request, 'postedit.html', {'onepost' : onepost})

def postupdate(request, post_id):
    onepost = get_object_or_404(Routine, pk=post_id)
    onepost.title = request.POST['title']
    onepost.url1 = request.POST['url1']
    onepost.part1 = request.POST['part1']
    onepost.url2 = request.POST['url2']
    onepost.part2 = request.POST['part2']
    onepost.save()
    return redirect('routinepage/detail/'+str(post_id))

def postdelete(request, post_id):
    onepost = get_object_or_404(Routine, pk=post_id)
    onepost.delete()
    return redirect('routinepage:home')

def commentcreate(request,post_id):
    if(request.method=='POST'):
        post = get_object_or_404(Routine,id=post_id)
        post.comment_set.create(title=request.POST['comment_content'])
    return redirect('/routinepage/detail/'+str(post_id))

def commentdelete(request,post_id,comment_id):
    comment = get_object_or_404(Comment,id=comment_id,routine_id=post_id)
    comment.delete()
    return redirect('/routinepage/detail/'+str(post_id))
