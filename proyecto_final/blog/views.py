from django.shortcuts import render
from .models import Post, Category, Author,Job,Donation,Collaboration,Donation_Goal
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from datetime import date
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

def postlist (request,slug):
    context = {
        'posts': '',
        'category': '',
    }
    return render(request, 'post_list.html', context)



@csrf_exempt
def dona(request):
    
    if(request.method == 'GET'):
        context = {
            'posts': '',
            'category': '',
        }
        return render(request, 'dona.html', context)
    

    
    if(request.method == 'POST'):
        firtsname = request.POST["floating_first_name"]
        lastname = request.POST["floating_last_name"]
        telephone = request.POST["floating_phone"]
        company = request.POST["floating_company"]
        email = request.POST["floating_email"]
        dateofbirht = request.POST["floating_date"]
        jobrol = request.POST["floating_job"]   
        payment = request.POST["floating_range"]        
        
        print("firtsname", firtsname)
        print("lastname", lastname)
        print("telephone", telephone)
        print("company", company)
        print("email", email)
        print("dateofbirht", dateofbirht)
        print("jobrol", jobrol)
        print("payment", payment)
        breakpoint()
        
        jobrol = Job.objects.filter(jobrol=f"{jobrol}").first()
        donation_Goal = Donation_Goal.objects.filter(active=f"{1}").first()

        if len(donation) == 0:
            print("payment", payment)
            
            # donation = Donation(
            #     firtsname=firtsname,
            #     lastname=lastname,
            #     telephone=telephone,
            #     company=company,
            #     email=email,
            #     dateofbirht=dateofbirht,
            #     createdate=date.today(),
            #     jobrol = jobrol,
            #     donation = 
            # )
            # donation.save()
        else:
            donation = donation.first()

        # collaboration = Collaboration(
        #     payment=payment,jobrol=jobrol , createdate=date.today(), donation=donation
        # )
        # collaboration.save()


        # # # # # # # # donation = Donation.objects.all().order_by("-id")
        # # # # # # # # collaboration = Collaboration.objects.all()
        # # # # # # # # job = Job.objects.all()

        # print(collaboration)

    # # #     diccionario = {"donation": donation, "collaboration": collaboration, "job": job}
    # # #     template = loader.get_template("gracias.html")

    # # # res = template.render(diccionario)
    # # # return HttpResponse(res)

    context = {
        'posts': '',
        'category': '',
    }
    return render(request, 'thanks.html', context)


# def dona(request):
#     context = {
#         'posts': '',
#         'category': '',
#     }
#     return render(request, 'dona.html', context)
