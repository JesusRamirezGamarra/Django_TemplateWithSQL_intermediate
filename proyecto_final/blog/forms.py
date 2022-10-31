from django import forms
#from django.forms import ModelForm
from ckeditor.fields import RichTextField,RichTextFormField
from .models import PostUserColaborator,UserColaborator

class CreateFormEmbrace(forms.Form):
    required_css_class = 'xst'
    name = forms.CharField(label="Nombre del adoptante",
                        max_length=50,
                        required=True,
                        widget=forms.TextInput(attrs={
        'class':'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'})
        
    )
    email = forms.EmailField(label="email del adoptante",
                        required=False,
                        widget=forms.TextInput(attrs={
        'class':'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'})
                        )
    description = forms.CharField(label="Descripcion de la motivacion del  adoptante",
                        required=False,
                        widget=forms.Textarea(attrs={
        'class':'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}),
                        )
    # description = RichTextFormField()
    


class UserColaboratorForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(), required=True, max_length=70)
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    pwd = forms.CharField(label='password', widget=forms.PasswordInput(),required=True, max_length=100)

    class Meta:
        model  = UserColaborator
        # fields = ['username','name','pwd','profile_picture']
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(),
            'name': forms.TextInput(),
            'pwd': forms.PasswordInput(),
            # 'profile_picture': forms.ImageField(),
            
        }
        # ordering = ("username")
    

class PostUserColaboratorForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
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
        
class EditarPerfilFormulario(forms.Form):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    profile_picture = forms.ImageField(required=False)