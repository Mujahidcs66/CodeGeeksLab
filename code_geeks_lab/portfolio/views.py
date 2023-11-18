from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CommentForm
from .models import Post, Comment

def post_detailview(request, id):
    
    if request.method == 'POST':
        cf = CommentForm(request.POST or None)
        if cf.is_valid():
            post = Post.objects.get(id=id)
            content = request.POST.get('content')
            comment = Comment.objects.create(post = post, commented_by = request.user, content = content)
            comment.save()
            return redirect('comments')
        
    cf = CommentForm()
    
    context ={
    'comment_form': cf,
    }
    return render(request, 'post_detail.html', context)

def comments(request):
    return HttpResponse("All Comments")