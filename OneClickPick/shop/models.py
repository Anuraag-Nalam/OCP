from django.db import models
'''THE FIRST MODEL WHIHCH IS NAMED AFTER THE CLASS PRODUCT IS RETRIEVING FROM THE DATABASE AND PUTTING THE
INFORMATION IN THE FRONT END WHERE AS IN CASE OF THE CLASS CONTACT, THE INFORMATION IS TAKEN FROM THE FRONT END AND
THEN IT IS KEPT IN THE DATABASE

A MODEL IS A SINGLE DEFINITIVE SOURCE OF INFORMATION ABOUT YOUR DATA. IT CONTAINS THE ESSENTIAL FIELDS AND BEHAVIOUR
OF THE DATA YOU ARE STORING. GENERALLY EACH MODEL MAPS TO A SINGLE DATABASE TABLE.
Create your models here. By default the models which we have created over here are stored in the sqlite database.
whatever apps we have created, they will definitely utilize either of the tables definitely. these apps definitely
uses the table in order to store the data.

when we run the command python manage.py runserver then it will talk about migrations telling that there are some unapplied
migrations which means that whatever installed apps are present in the project settings.py file, they use the tables(as
discussed above) and we have'nt created them and we can create them by  making migrations. we have to run the command
python manage.py make migrations which means that we are telling django to store the changes whatever we have created and
there is another command called as python manage.py migrate which
creates the tables required for the apps and put it in the database.

MIGRATION MEANS WHATEVER CHANGE WE ARE DOING, WE ARE
STORING IT. HERE WE ARE NOT CHANGING THE DATABASE. WE ARE JUST STORING THE INFORMATION IN THE DATABASE THAT WE ARE DOING
THESE CHANGES.

If we apply these migrations then we have applied the migrations.
FOR example there is a table called as products and we want to change its name to goodproducts. then we are just
saving these changes in the data base by using the command python manage.py make migrations.
when we apply these migrations then we change our database.'''
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=70)
    desc=models.CharField(max_length=1000)
    pub_date=models.DateField()
    price=models.IntegerField(default=0)
    category=models.CharField(max_length=50,default='')
    subcategory=models.CharField(max_length=55,default="")
    image=models.ImageField(upload_to='shop/images',default='')
    def __str__(self):
        return self.product_name
class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    text=models.CharField(max_length=1000,default="")
    email=models.CharField(max_length=70,default="")
    phone=models.CharField(max_length=20,default="")
    def __str__(self):
        return self.name
class Order(models.Model):
    order_id=models.AutoField(primary_key= True)
    items_json=models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=5000)
    email=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=50)
    phone=models.CharField(max_length=50,default="")
class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default='')
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+"..."

''' these migrations are stored in 0001_initial.py file.SO AS TO CHECK WHETHER THE MIGRATIONS HAS ACTUALLY HAPPENED OR NOT,
WE HAVE O CREATE A SUPER USER AND IT IS EXPLAINED OVER HERE.USING THIS WE CAN CHECK WHAT CHANGES WE HAVE DONE IN OUR
DATABASE. SO AS TO ADD THE PRODUCTS WE HAVE TO MAKE A SUPER USER. THIS SUPER USER HAS THE POWER TO DO EVERYTHING'''
'''YOU CAN ALSO FETCH THE PRODUCTS USING THE POWER SHELL OR THE TERMINAL OF THE PYCHARM ITSELF. THERE IS NO NEED TO VISIT THE DJANGO ADMIN
PAGE ALWAYS. WE CAN ALSO ADD THE PRODUCTS USING THE SHELL IT SELF BY CREATING A VARIABLE CALLED AS MYPROD AND ADDING ALL THE FIELDS INTO IT
THEN WE CAN ACCESS THE NAMES USING THESE FIELDS. FOR EXAMPLE, IF WE WANT A NAME OF THE OBJECT AS PURSE, THEN WE HAVE TO ACCESS IT AS
MYPROD.product_name. THE COMMAND project.objects.all will fetch out all the objects available in the database.'''
