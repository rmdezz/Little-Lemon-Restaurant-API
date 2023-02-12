# Import the necessary modules for defining models in Django
from django.db import models 
# Import the built-in User model
from django.contrib.auth.models import User 

# A field will be indexed in the database for faster querying (db_index = True)

# db_index=True in Django is a flag that tells the database to create an index
# for the field. An index is a data structure that allows the database to quickly
# locate and retrieve the data for a specific field.

# An index does not create a copy of the values in the database. Instead, it creates
# a separate data structure that maps the values in the field to their location in
# the table. This mapping allows the database to quickly find the relevant rows when
# querying the field.

# When you update a value of an entry after indexing, the index is automatically updated
# to reflect the changes. This is because the index is linked to the data in the database,
# and any changes to the data will also be reflected in the index.

# Create your models here.

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True) 
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        unique_together = ('menuitem', 'user') # a Cart object cannot have duplicate menuitem and user combinations.

class Order(models.Model):
    # on_delete = models.CASCADE => deletion of a User will also result in deletion of the associated Order objects. 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # on_delete = models.SET_NULL => if a User is deleted, the associated delivery_crew field will be set to NULL
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="delivery_crew", null=True)
    status = models.BooleanField(db_index=True, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(db_index=True)
    
class OrderItem(models.Model):
    # on_delete = models.CASCADE => deletion of a User will also result in deletion of the associated OrderItem objects. 
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    # on_delete = models.CASCADE => deletion of a MenuItem will also result in deletion of the associated OrderItem objects. 
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        unique_together = ('order', 'menuitem') # a OrderItem object cannot have duplicate order and menuitem combinations.
        
        