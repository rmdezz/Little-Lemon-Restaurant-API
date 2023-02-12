from rest_framework import serializers
from .models import MenuItem, Category, Cart, Order, OrderItem
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True) # for GET requests
    category_id = serializers.IntegerField(write_only = True) # for POST, PUT, PATCH requests, it won't appear in GET requests
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category', 'category_id']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        
class CartItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Cart
        fields = ('id', 'user', 'menuitem', 'quantity', 'unit_price', 'price')
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'menuitem', 'quantity', 'unit_price', 'price']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(read_only = True, many = True)
    class Meta:
        model = Order
        fields = ('id', 'user', 'delivery_crew', 'status', 'order_items', 'total', 'date')
        
class OrderDetailSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(read_only = True, many = True)
    class Meta:
        model = Order
        fields = ('order_items', )