from django.shortcuts import render
from .models import Post, Category, Author
from django.db.models import Q
# Create your views here.

def homepage(request):
    categories = Category.objects.all()[0:4]
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context= {
        'object_list': featured,
        'latest': latest,
        'categories':categories,
    }
    return render(request, 'homepage.html', context)

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    # breakpoint()
    # print(context)
    return render(request, 'search_bar.html', context)

def allposts(request):
    posts = Post.objects.order_by('-timestamp')
    context = {
        'posts': posts,
    }
    # print(context)
    return render(request, 'all_posts.html', context)

def post(request,slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'post.html', context)



# def category_post_list (request, slug):
#     category = Category.objects.get(slug = slug)
#     posts = Post.objects.filter(categories__in=[category])
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'post_list.html', context)


# def postlist (request,slug):
#     category = Category.objects.get(slug = slug)
#     posts = Post.objects.filter(categories__in=[category])

#     context = {
#         'posts': posts,
#         'category': category,
#     }
#     return render(request, 'post_list.html', context)

