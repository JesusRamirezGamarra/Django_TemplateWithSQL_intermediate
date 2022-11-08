from django.test import TestCase
from .forms import CreateFormEmbrace
from .models import Embrace
from django.db.models import Q

# Create your tests here.
# e.g ejecucion directa : python manage.py test blog.tests.CreateFormEmbrace_FormTest
class CreateFormEmbrace_FormTest(TestCase):    
    @classmethod
    def setUpTestData(cls):
        print('-'* 100)
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        donation_user01 = 'John Snow'
        email_user01 = 'Jhon.Snow@Stark.info'
        donation_user02 = 'John smith'
        email_user02 = 'Jhon.Smith@Matrix.info'
        number_of_Embrace_request = 30
        for item in range(number_of_Embrace_request):
            
            if item % 2:
                Embrace.objects.create(
                    name = donation_user01,
                    email = email_user01,
                    description = 'motivation : '+ str(item)
                )
            else:
                Embrace.objects.create(
                    name = donation_user02,
                    email = email_user02,
                    description = 'motivation : '+str(item)
                )

    def setUp(self):
        print('-'* 100)
        print("setUp: Run once for every test method to setup clean data.")
    
    def test_createformembrace_form_name_field_label(self):
        print("Method: test_createformembrace_form_name_field_label assertTrue.")        
        form = CreateFormEmbrace()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Nombre del adoptante')
        
    def test_createformembrace_form_name_field_help_text(self):
        print("Method: test_createformembrace_form_name_field_help_text assertEqual.")      
        form = CreateFormEmbrace()
        self.assertEqual(form.fields['name'].help_text,'Enter a Full name . e.g Jhon Snow')       
        self.assertEqual(form.fields['email'].help_text,'Enter a email . e.g Jhon.Snow@Stark.info')
        self.assertEqual(form.fields['description'].help_text,'motivation . e.g I want to have a new best friend who is by my side unconditionally...')

    def test_createformembrace_form_data_in_past(self):
        print("Method: test_createformembrace_form_data_in_past assertTrue.")      
        form_data = {
            'name': 'John Snow',
            'email': 'Jhon.Snow@Stark.info',
            'description': 'I want to have a new best friend who is by my side unconditionally...'
        }
        form = CreateFormEmbrace(data=form_data)
        self.assertTrue(form.is_valid())        
        
    def test_createformembrace_form_notdata_in_past(self):
        print("Method: test_createformembrace_form_notdata_in_past assertFalse.")      
        form_data = {}
        form = CreateFormEmbrace(data=form_data)
        self.assertFalse(form.is_valid())              
        

    def test_createformembrace_form_count(self):
        print("Method: test_createformembrace_form_count assertEqual.")      
        self.embrace = Embrace.objects.filter(Q(name='John Snow') )
        self.assertEqual(len(self.embrace.all())   ,15)             