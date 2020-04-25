from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).all()
    template_name = 'blog/home.html'
    paginate_by = 5

def PostDetail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    #Comment Posted
    if request.method == 'POST':
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    else:
        comment_form = CommentForm()
    
    return render(request, template_name, {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    })

