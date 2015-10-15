from django.shortcuts import render, HttpResponse, get_object_or_404

from blog.models import Post

# Create your views here.
def index(request):
    post_list = Post.objects.order_by('-pub_date')
    context_dict = {'post_list': post_list}
    return render(request, "blog/index.html", context_dict)