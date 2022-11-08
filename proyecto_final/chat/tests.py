from django.test import TestCase
from .models import Room,Message
from django.db.models import Q

# Create your tests here.
# e.g ejecucion directa : python manage.py test chat.tests.Room_TestCase
class Room_TestCase(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        print('-'* 100)
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        Room.objects.create(name='TEST ROOM ONE')
        Room.objects.create(name='TEST ROOM TWO')            
    
    def setUp(self):
        print('-'* 100)
        print("setUp: Run once for every test method to setup clean data.")
                
    def test_add_new_room(self):
        print("Method: test_add_new_room assertEqual.")
        self.room = Room.objects.filter(Q(name='TEST ROOM ONE') | Q(name='TEST ROOM TWO'))
        self.assertEqual(len(self.room.all())   ,2)

    def test_name_label(self):
        print("Method: test_name_label assertEquals.")   
        room=Room.objects.get(name='TEST ROOM ONE')
        field_label = room._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')
        
    def test_date_of_created_label(self):
        print("Method: test_date_of_created_label assertEquals.")   
        room=Room.objects.get(name='TEST ROOM ONE')
        field_label = Room._meta.get_field('created').verbose_name
        self.assertEquals(field_label,'Fecha de creación')     
        
    def test_first_name_max_length(self):
        print("Method: test_first_name_max_length assertTrue.")   
        room=Room.objects.get(id=1)
        max_length = room._meta.get_field('name').max_length
        self.assertTrue( max_length == 100)           
                    
    def test_object_def_str(self):
        print("Method: test_object_def_str assertTrue.")           
        room=Room.objects.get(name='TEST ROOM ONE')
        expected_object_str = '%s %s' % (room.name, room.created)
        self.assertEquals(expected_object_str,str(room))
                    
# e.g ejecucion directa : python manage.py test chat.tests.Message_TestCase 
class Message_TestCase(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        print('-'* 100)        
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        room = Room.objects.create(name='ROOM Group')
        Message.objects.create(value='Hello Word Messenger CHAT BFFs [0]',user='Jesus Ramirez',room=room)
        Message.objects.create(value='Hello Word Messenger CHAT BFFs [1]',user='Jhon Snow',room=room)
        
    def setUp(self):
        print('-'* 100)        
        print("setUp: Run once for every test method to setup clean data.")

    def test_add_new_message(self):
        print("Method: test_add_new_message assertEqual.")
        self.message = Message.objects.filter(Q(value='Hello Word Messenger CHAT BFFs [0]') | Q(value='Hello Word Messenger CHAT BFFs [1]'))
        self.assertEqual(len(self.message.all())   ,2)        
        
    def test_name_label(self):
        print("Method: test_name_label assertEquals.")   
        message=Message.objects.get(value='Hello Word Messenger CHAT BFFs [0]')
        field_label = message._meta.get_field('value').verbose_name
        self.assertEquals(field_label,'value')
        
    def test_date_of_created_label(self):
        print("Method: test_date_of_created_label assertEquals.")   
        message=Message.objects.get(value='Hello Word Messenger CHAT BFFs [0]')
        field_label = message._meta.get_field('created').verbose_name
        self.assertEquals(field_label,'Fecha de creación')     
        
    def test_first_name_max_length(self):
        print("Method: test_first_name_max_length assertFalse.")   
        message=Message.objects.get(value='Hello Word Messenger CHAT BFFs [0]')
        max_length = message._meta.get_field('value').max_length
        self.assertFalse( max_length == 100)           
                    
    def test_object_def_str(self):
        print("Method: test_object_def_str assertTrue.")           
        message=Message.objects.get(value='Hello Word Messenger CHAT BFFs [0]')
        expected_object_str = '%s %s' % (message.room, message.user)
        self.assertEquals(expected_object_str,str(message))