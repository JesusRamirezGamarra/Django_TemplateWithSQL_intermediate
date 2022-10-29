from django.shortcuts import render
from .models import Post, Category, Author,Job,Donation,Collaboration,Donation_Goal,Contact,Embrace, PostUserColaborator, UserColaborator
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from django.db.models import Sum,Count
from .forms import CreateFormEmbrace,PostUserColaboratorForm
from django.views.generic.list import ListView


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
    category = Category.objects.get(slug = slug)
    posts = Post.objects.filter(categories__in=[category])

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_list.html', context)

def category_post_list (request, slug):
    category = Category.objects.get(slug = slug)
    posts = Post.objects.filter(categories__in=[category])
    context = {
        'posts': posts,
    }
    return render(request, 'post_list.html', context)


@csrf_exempt
def dona(request):
    
    if(request.method == 'GET'):
        donation_Goal = Donation_Goal.objects.filter(active=f"{1}").first()
        result_net = Collaboration.objects.aggregate(total_amount=Sum('amount'))
        result = Collaboration.objects.values('donation').annotate(total_amount=Sum('amount'))
        # print(result_net)
        # print(result)

        context = {
                    "donation_Goal":donation_Goal,
                    "total_amount":result_net['total_amount'],
                    'need_to_donate': donation_Goal.goal - result_net['total_amount']
                    }
        return render(request, 'dona.html', context)
    
    if(request.method == 'POST'):
        firtsname = request.POST["floating_first_name"]
        lastname = request.POST["floating_last_name"]
        telephone = request.POST["floating_phone"]
        company = request.POST["floating_company"]
        email = request.POST["floating_email"]
        dateofbirht = request.POST["floating_date"]
        job_id = request.POST["floating_job"]   
        amount  = request.POST["floating_range"]        
        
        # print("firtsname", firtsname)
        # print("lastname", lastname)
        # print("telephone", telephone)
        # print("company", company)
        # print("email", email)
        # print("dateofbirht", dateofbirht)
        # print("jobrol_id", job_id)
        # print("payment", amount )

        
        job = Job.objects.filter(id=f"{job_id}").first()
        donation_Goal = Donation_Goal.objects.filter(active=f"{1}").first()
        donation = Donation.objects.filter(email=f"{email}")

        if len(donation) == 0:
            print("payment", donation)
            
            donation = Donation(
                firtsname=firtsname,
                lastname=lastname,
                telephone=telephone,
                company=company,
                email=email,
                dateofbirht=dateofbirht,
                createdate=date.today(),
                job = job,
                donation_Goal =  donation_Goal
            )
            donation.save()
        else:
            donation = donation.first()

        collaboration = Collaboration(
            amount =amount ,
            createdate=date.today(), 
            job=job , 
            donation=donation
        )
        collaboration.save()


        donationAll = Donation.objects.all().order_by("-id")
        collaboration = Collaboration.objects.all()
        job = Job.objects.all()
        result_net = Collaboration.objects.aggregate(total_amount=Sum('amount'))
        result = Collaboration.objects.values('donation').annotate(total_amount=Sum('amount'))
        print(result_net)
        print(result)
        
        # breakpoint()
        context = {"donation": donationAll, 
                    "collaboration": collaboration, 
                    "job": job,
                    "donation_Goal":donation_Goal,
                    "donationLast": donation,
                    "amount": amount,
                    "result_net":result_net,
                    "result":result,
                    'need_to_donate': donation_Goal.goal - result_net['total_amount']
                    }
        return render(request, 'thanks.html', context)

@csrf_exempt
def contact(request):
    
    if request.method == 'GET':
        return render(request, 'contact.html')
    
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]        
        message = request.POST["message"]    
        print(request.POST)        
        Contact.objects.create(
            email= email,
            subject= subject,
            message= message
        )        
        context = {
            'result': {'name': name,'email': email},
        }
        return render(request, 'contact.html',context)

@csrf_exempt
def embrace(request):
    if request.method == 'GET':
        formEmbrace = CreateFormEmbrace(auto_id=False)    
        return render(request, 
                    'embrace.html', 
                    {
                        'form': formEmbrace,
                    }
        )
        
    if request.method == 'POST':
        # name = request.POST["name"]
        # email = request.POST["email"]
        # description = request.POST["description"]
        # print(request.POST)        
        formEmbrace = CreateFormEmbrace(request.POST)   
        
        if formEmbrace.is_valid() :

            info = formEmbrace.cleaned_data
            name = info["name"]
            email = info["email"]
            description = info["description"]            
            # print(info)
            Embrace.objects.create(
                                name = name,
                                email = email,
                                description = description
                            )

            return render(request, 
                        'embrace.html', 
                        {
                            'form': formEmbrace,
                            'result': {'name': name,'email': email},
                        }
            )
            
def about (request):
    return render(request, 'about.html')



class AddPostView(ListView):
    model = PostUserColaborator

    print ('AddPostView')
    
    def get(self, request):
        form = PostUserColaboratorForm()
        return render(request, 'add_post_colaborator.html', {'form':form})
    def post(self, request):
        form = PostUserColaboratorForm(request.POST)
        if form.is_valid():
            userName = form.cleaned_data['userName']
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            user_obj = UserColaborator.objects.get(user_name=userName)
            add_post = PostUserColaborator.objects.create(user=user_obj, title=title, content=content)
            add_post.save()
            form = PostUserColaboratorForm()
            return render(request,'add_post_colaborator.html',{'form':form})

class AllPostView_list(AddPostView):
    model = PostUserColaborator
    
    def get(self,request):
        all_post = self.model.objects.all().order_by('-createdate')
        print(all_post)
        return render(request, 'all_post_colaborator.html', {'posts':all_post})

def AllPostView(request, slug):
    userColaborator = UserColaborator.objects.get(username = slug)
    # print('userColaborator',userColaborator)
    # breakpoint()
    postUserColaborator = PostUserColaborator.objects.filter(user= userColaborator).order_by('-createdate')
    context = {
        'posts': postUserColaborator,
    }
    return render(request, 'all_post_colaborator.html', context)    
    
    # model = PostUserColaborator
    
    # def get(self,request):
    #     all_post = self.model.objects.all().order_by('-id')
    #     print(all_post)
    #     print(all_post.user.profile_picture.url)
    #     return render(request, 'all_post_percolaborator.html', {'posts':all_post})
