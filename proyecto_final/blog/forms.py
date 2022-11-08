from django import forms
#from django.forms import ModelForm
from ckeditor.fields import RichTextField,RichTextFormField
from .models import PostUserColaborator,UserColaborator,Suscripcion,Perfil

class CreateFormEmbrace(forms.Form):
    required_css_class = 'xst'
    name = forms.CharField(label="Nombre del adoptante",
                        max_length=50,
                        required=True,
                        widget=forms.TextInput(attrs={
        'class':'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}),
                        help_text="Enter a Full name . e.g Jhon Snow"
        
    )
    email = forms.EmailField(label="email del adoptante",
                        required=False,
                        widget=forms.TextInput(attrs={
        'class':'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}),
                        help_text="Enter a email . e.g Jhon.Snow@Stark.info"
    )
    description = forms.CharField(label="Descripcion de la motivacion del adoptante",
                        required=False,
                        widget=forms.Textarea(attrs={
        'class':'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}),
                        help_text="motivation . e.g I want to have a new best friend who is by my side unconditionally..."
    )
    # description = RichTextFormField()
    


class UserColaboratorForm(forms.ModelForm):
    # username = forms.CharField(widget=forms.TextInput(), required=True, max_length=70)
    # name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    # pwd = forms.CharField(label='password', widget=forms.PasswordInput(),required=True, max_length=100)

    class Meta:
        model  = UserColaborator
        # fields = ['username','name','pwd','profile_picture']
        fields = '__all__'
        # widgets = {
        #     'username': forms.TextInput(),
        #     'name': forms.TextInput(),
        #     'pwd': forms.PasswordInput(),
        #     # 'profile_picture': forms.ImageField(),
            
        # }
        # ordering = ("username")
    

class PostUserColaboratorForm(forms.ModelForm):
    # username = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    title = forms.CharField(widget=forms.TextInput(),required=True, max_length=100)
    content = RichTextField()

    class Meta:
        model  = PostUserColaborator
        fields = '__all__'
        # fields = ('username','title','content')



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    
    # username = forms.CharField(label='Usuario', required=True, max_length=20)
    email = forms.EmailField()
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Re Password',widget=forms.PasswordInput)
    
    class Meta:  
        model = User
        fields = ['username','email','password1','password2']
        # fields =  '__all__'
        help_texts = {key:'' for key in fields} #listComprension aplica para duplas y dictorionarys
        
        
# Options = (
#         ('1', 'Hello'),
#         ('2', 'World'),
# )
def ListarSuscripcion():
    # suscripcion = Suscripcion.objects.all().order_by("-id")
    # print(suscripcion)
    result = Suscripcion.objects.all().values_list("id", "name")
    # print(result)
    return list(result)
    # print(result)
    # # return result
    # return  (
    #         ('1', 'Hello'),
    #         ('2', 'World'),
    # )
            
class EditarPerfilFormulario(forms.Form):
    profile_picture = forms.ImageField( label='Avatar', 
        #                                 widget=forms.ClearableFileInput(attrs={
        # 'class':'block w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 cursor-pointer dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400',
        # }),
                                        required=False
    )
    first_name = forms.CharField(   label='Nombre'  ,
                                    widget=forms.TextInput(attrs={
        'class':'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 dark:shadow-sm-light',
        'placeholder': 'Ingresa tus Nombres(s) : eg John Luis',        
        })
    )
    last_name = forms.CharField(    label='Apellido',
                                    widget=forms.TextInput(attrs={
        'class':'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 dark:shadow-sm-light',
        'placeholder': 'Ingresa tus Apellidos(s) : eg Snow Sanchez',        
        })
    )
    email = forms.EmailField(   label='Email Principal: ',
                                widget=forms.TextInput(attrs={
        'class':'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 dark:shadow-sm-light',
        'placeholder': 'Ingresa tu Email : eg Jhon.Snow@CoderHouse.info',
        })
    )
    email_colaborator = forms.EmailField(   label='Email Secundario (Colaborador):',
                                widget=forms.TextInput(attrs={
        'class':'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 ,dark:shadow-sm-light',
        'placeholder': 'Ingresa tu Email : eg Jhon.Snow@CoderHouse.info',
        })                                         
    )
    description = forms.CharField(  widget=forms.Textarea(attrs={
        'class':'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg shadow-sm border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500',
        'rows':'8',
        }), 
    )
    perfil =  forms.ChoiceField(    label='Perfil', 
                                    widget=forms.Select(attrs={
        'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        }), 
                                    choices=list(Perfil.objects.all().values_list("id", "name") ) ,
                                    required = True,
                                )
    suscripcion = forms.ChoiceField(    label='Suscripcion', 
                                        widget=forms.Select(attrs={
        'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        }), 
                                    choices=ListarSuscripcion(),
                                    required = True,                                        
    )
#    field_name = forms.ModelChoiceField(queryset=Position.objects.all(),
#         empty_label="(Select here)")
       
    
    #     name = forms.CharField(label="Nombre del adoptante",
    #                     max_length=50,
    #                     required=True,
    #                     widget=forms.TextInput(attrs={
    #     'class':'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'})
        
    # )
    
    