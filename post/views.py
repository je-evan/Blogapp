from django.views import generic
from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q


class PostList(generic.ListView):
    template_name = 'post_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        search = self.request.GET.get('search', '')
        print(search)
        object_list = Post.objects.filter(status=1).order_by('-created_on')
        if search:
            object_list = object_list.filter(Q(title__icontains=search) | Q(content__icontains=search))
            if object_list:
                messages.success(self.request, f'The results found for "{search}" are:')
            else:
                messages.warning(self.request, f'No result found for "{search}"\nclick "Blog" on menu bar to see all blogs')
        return object_list

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.post_comments.filter(active=True, reply_of=None)
    replies = post.post_comments.filter(active=True).exclude(reply_of=None)
    comment_form = CommentForm() 

    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                cmnt_id = request.POST.get('reply', '')
                if cmnt_id:
                    new_reply = comment_form.save(commit=False)
                    new_reply.post = post
                    new_reply.commented_by = request.user
                    new_reply.reply_of = post.post_comments.get(id=cmnt_id)
                    new_reply.save()
                    messages.success(request, 'Your reply is awaiting moderation!')
                else:
                    new_comment = comment_form.save(commit=False)
                    new_comment.post = post
                    new_comment.commented_by = request.user
                    new_comment.save()
                    messages.success(request, 'Your comment is awaiting moderation!')
            comment_form = CommentForm()
        else:
            messages.warning(request, 'You have to login to comment!')
            return redirect('login')

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'comment_form': comment_form,
                                           'replies': replies})
