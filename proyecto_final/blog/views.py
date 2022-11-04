from django.shortcuts import render,redirect
from .models import Post, Category, Author,Job,Donation,Collaboration,Donation_Goal,Contact,Embrace, PostUserColaborator, User, UserColaborator,Perfil,Suscripcion
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from django.db.models import Sum,Count
from .forms import CreateFormEmbrace,PostUserColaboratorForm,EditarPerfilFormulario
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required


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
            # print("payment", donation)
            
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
        # print(result_net)
        # print(result)
        
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
        # print(request.POST)        
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

    def get(self, request):
        form = PostUserColaboratorForm()
        return render(request, 'add_post_colaborator.html', {'form':form})
    def post(self, request):
        form = PostUserColaboratorForm(request.POST)
        if form.is_valid():
            # userName = form.cleaned_data['userName']
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            # user = UserColaborator.objects.get(user_name=userName)
            user = request.user
            add_post = PostUserColaborator.objects.create(user=user, title=title, content=content)
            add_post.save()
            form = PostUserColaboratorForm()
            return render(request,'add_post_colaborator.html',{'form':form})

class AllPostView_list(AddPostView):
    model = PostUserColaborator
    
    def get(self,request):
        all_post = self.model.objects.all().order_by('-createdate')
        # print(all_post)
        return render(request, 'all_post_colaborator.html', {'posts':all_post})

# @login_required(login_url='/login')
def allPostView(request, slug):
    user = User.objects.get(username = slug)
    userColaborator = UserColaborator.objects.get(user = user)
    postUserColaborator = PostUserColaborator.objects.filter(user= user).order_by('-createdate')
    context = {
        'posts': postUserColaborator,
    }
    return render(request, 'all_post_colaborator.html', context)    

#############################################
# CRUD + Detail
#############################################

from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class Create_UserPostColaborator(LoginRequiredMixin,CreateView):
    model = PostUserColaborator
    template_name = 'CRUD/create_post_colaborator.html'
    success_url = '/post_colaborator/read/'
    fields = '__all__'
    # fields = ['title','content']
    login_url = '/login/'    
    
    def form_valid(self, form):
        # breakpoint()
        self.object = form.save()
        return redirect(self.get_success_url())

class Read_UserPostColaborator(ListView):
    model = PostUserColaborator
    template_name = 'CRUD/read_post_colaborator.html'
    fields = '__all__'    
    login_url = '/login/'               
    ordering = ['-createdate']
    
    def get_queryset(self):
        queryset = PostUserColaborator.objects.filter(user= self.request.user.id)
        #User.objects.filter(username=f"{ request.POST['username']}").first()
        # if self.request.GET.get("browse"):
        #     selection = self.request.GET.get("browse")
        #     if selection == "Cats":
        #         queryset = Cats.objects.all()
        #     elif selection == "Dogs":
        #         queryset = Dogs.objects.all()
        #     elif selection == "Worms":
        #         queryset = Worms.objects.all()
        #     else:
        #         queryset = Cats.objects.all()
        return queryset
    
    # def get_queryset(self, *args, **kwargs):
    #     qs = super(Read_UserPostColaborator, self).get_queryset(*args, **kwargs)
    #     qs = qs.order_by("createdate")
    #     return qs    

class Update_UserPostColaborator(LoginRequiredMixin,UpdateView):
    model = PostUserColaborator
    template_name = 'CRUD/update_post_colaborator.html'
    success_url = '/post_colaborator/read/'
    fields = '__all__'    
    login_url = '/login/'    
    
    def form_valid(self, form):
        # breakpoint()
        self.object = form.save()
        return redirect(self.get_success_url())   
    
# def get_queryset(self):
#         queryset = PostUserColaborator.objects.filter(user= self.request.user.id)
#         return queryset            

class Delete_UserPostColaborator(LoginRequiredMixin,DeleteView):
    model = PostUserColaborator
    template_name = 'CRUD/delete_post_colaborator.html'
    success_url = '/post_colaborator/read/'    
    fields = '__all__'    
    login_url = '/login/'               

class Detail_UserPostColaborator():
    pass


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from .forms import UserRegisterForm

def login(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    
    if request.method == 'GET':
        formulario = AuthenticationForm()
        result =  lambda a=1,b=2: str(random.randint(a,b)) +'.jpg'
        context = {
                'formulario':formulario,
                'result': {'image': result(1,26)},
        }        
        return render(request, 'private/login.html',context)    
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request,data= request.POST)
        # print(formulario)

        if formulario.is_valid():
            user = formulario.get_user()
            django_login(request,user)
            return redirect('homepage')
        else:
            result =  lambda a=1,b=2: str(random.randint(a,b)) +'.jpg'
            context = {
                'formulario':formulario,
                'result': {'image': result(1,26)},
                'error' : {'detalle':'Usuario o Contrasena errados,Re intente nuevamente ...'}
            }    
            return render(request, 'private/login.html',context)                       
            # return redirect('login')
    
    
    
    
    
    
# from django.contrib.auth.forms import UserCreationForm
# def registrar(request):
#     if request.method == 'POST':
#         formulario = UserCreationForm(request.POST)
#         if formulario.is_valid():
#             formulario.save()
#             return redirect('homepage')
#     else: 
#         formulario = UserCreationForm()
#     return render(request, 'private/registrar.html',{'formulario':formulario})

def registrar(request):
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            user = User.objects.filter(username=f"{ request.POST['username']}").first()
            # print(user)
            # breakpoint()
            
            userColaborator, es_NuevoUserColaborator = UserColaborator.objects.get_or_create(user = user)
            return redirect('homepage')
    else: 
        formulario = UserRegisterForm()
    return render(request, 'private/registrar.html',{'formulario':formulario})

@login_required(login_url='/login')
def perfil(request):
    # formulario = UserRegisterForm(request.POST)
    #crea el objeto  UserColaborator si no existe
    userColaborator, es_NuevoUserColaborator = UserColaborator.objects.get_or_create(user = request.user)
    # print(userColaborator)
    # print(es_NuevoUserColaborator)
    # breakpoint()
    return render(request, 'private/perfil.html',{'formulario':{}})

@login_required(login_url='/login')
def perfil_editar(request):
    # user = request.user # se podria realizar con la referencia a user en lugar de request.
    # user = request.user
    
    if request.method == 'POST':
        formulario = EditarPerfilFormulario(request.POST,request.FILES)
        
        if formulario.is_valid():
            datanueva = formulario.cleaned_data
            request.user.first_name = datanueva['first_name']
            request.user.last_name = datanueva['last_name']
            request.user.email = datanueva['email']
            request.user.usercolaborator.email = datanueva['email_colaborator']
            request.user.usercolaborator.description = datanueva['description']
            
            request.user.usercolaborator.perfil =  Perfil.objects.filter(id=f"{datanueva['perfil']}").first()
            # request.user.usercolaborator.perfil.id = datanueva['perfil']
            request.user.usercolaborator.suscripcion = Suscripcion.objects.filter(id=f"{datanueva['suscripcion']}").first()
            # request.user.usercolaborator.suscripcion.id = datanueva['suscripcion']
            if(datanueva['profile_picture'] != None ):
                request.user.usercolaborator.profile_picture = datanueva['profile_picture']
            # print(datanueva['profile_picture'])
            # print( datanueva['description'])                        
            # print( datanueva['perfil'])                        
            # print( datanueva['suscripcion'])                        
            # request.user.usercolaborator.perfil.save()
            request.user.usercolaborator.save()
            request.user.save()
            
            return redirect('perfil')
        
    else:
        formulario = EditarPerfilFormulario(
            initial={   'first_name': request.user.first_name, 
                        'last_name': request.user.last_name,
                        'email': request.user.email,
                        'email_colaborator': request.user.usercolaborator.email,
                        'description': request.user.usercolaborator.description,
                        'perfil': request.user.usercolaborator.perfil.id,
                        'suscripcion': request.user.usercolaborator.suscripcion.id,
                        'profile_picture' : request.user.usercolaborator.profile_picture
                    }
        )
    return render(request, 'private/perfil_editar.html',{'formulario':formulario})


from django.contrib.auth.views import PasswordChangeView
class Password_editar(LoginRequiredMixin,PasswordChangeView):
    template_name = 'private/password_editar.html'
    success_url = '/perfil/'
    login_url = '/login/'   
    # result =  lambda a=1,b=2: str(random.randint(a,b)) +'.jpg'
    # context = {
    #     'result': {'image': '1.jpg'},
    # }   
    # extra_context = context
    def post(self, request, *args, **kwargs):
        if request.POST["cancel"]:
            return redirect('perfil')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # result =  lambda a=1,b=2: str(random.randint(a,b)) +'.jpg'
        # context['result'] ={'image': result(1,20)}
        # print('s')
        # print(context)
        return context
    
    
    # model = PostUserColaborator
    # template_name = 'CRUD/update_post_colaborator.html'
    # success_url = '/post_colaborator/read/'
    # fields = '__all__'    
    # login_url = '/login/'    
        
    
import random

@login_required(login_url='/login')    
def  Logout(request):
    # template_name = 'private/logout.html'
    # login_url = '/login/'   
    result =  lambda a=1,b=2: str(random.randint(a,b)) +'.jpg'
    #result = result(1,20)+'.jpg'
    # print(result(1,20))        
    context = {
        'result': {'image': result(1,20)},
    }    
    # context = {
    # 'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']
    # }
    # {{context|random}}
    return render(request,'private/logout.html',context )         
