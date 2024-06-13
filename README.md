# Intro
This is my first DRF based Django project It's designed to showcase my skills in creating RESTful APIs using Django and DRF.

The project does not have a frontend using neither the template system nor independent frontend technologies. 

I've been keen on using CBVs instead of FBVs as much as I could since I find them greatly contributing to the clean code principles


# The account app 
- Uses the CustomUser model inheriting from AbstractUser model in order to manage user accounts and their relevant data
  
- In views.py, generic DRF's CreateAPIView is used to create CustomUser objects(user account), serializing the data using the RegisterSerializer from serializers.py,
and APIView for Loggin in and displaying a list of all users sotred by CustomUser table via the ListUser view.



# DRF API Views
A variaty of generic DRF API view have been used including CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView and the basic APIView in order to CRUD data. Used
both in account & todo_project apps.
