from datetime import date
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from .models import MenuItem, Category, Cart, Order, OrderItem
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import MenuItemSerializer, CategorySerializer, UserSerializer, CartItemSerializer, OrderSerializer, OrderDetailSerializer
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttles import OneCallPerMinute

# Create your views here.

# Menu-items views

@throttle_classes([AnonRateThrottle, UserRateThrottle])
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.select_related('category').all() # retrieve related objects in a single query
    serializer_class = MenuItemSerializer
    
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'price', 'category__slug']
    ordering_fields = ['title', 'price', 'category__slug']
    search_fields = ['category__slug']
    
    def get(self, request):
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('price')
        search = request.query_params.get('search')
        
        if category_name:
            self.queryset = self.queryset.filter(category__slug = category_name)
        if to_price:
            self.queryset = self.queryset.filter(price = to_price)
        if search:
            self.queryset = self.queryset.filter(category__slug__startswith = search)
        return super().get(request)
    
    def post(self, request):
        if request.user.groups.filter(name = 'Manager').exists() or request.user.is_superuser:
            return super().post(request)
        return Response({"message": "You are not authorized"}, status = status.HTTP_403_FORBIDDEN)
    
    def put(self, request, *args, **kwargs):
        if request.user.groups.filter(name = 'Manager').exists():
            return super().post(request)
        return Response({"message": "You are not authorized"}, status = status.HTTP_403_FORBIDDEN)

    def patch(self, request, *args, **kwargs):
        if request.user.groups.filter(name = 'Manager').exists():
            return super().post(request)
        return Response({"message": "You are not authorized"}, status = status.HTTP_403_FORBIDDEN)

    def delete(self, request, *args, **kwargs):
        if request.user.groups.filter(name = 'Manager').exists():
            return super().post(request)
        return Response({"message": "You are not authorized"}, status = status.HTTP_403_FORBIDDEN)
    
@throttle_classes([OneCallPerMinute, UserRateThrottle])  
class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        if request.user.groups.filter(name = 'Manager').exists():
            return super().put(request, *args, **kwargs)
        return Response({"message": "You are not authorized"}, status = status.HTTP_403_FORBIDDEN)
    
    def patch(self, request, *args, **kwargs):
        if request.user.groups.filter(name = 'Manager').exists():
            return super().patch(request, *args, **kwargs)
        return Response({"message": "You are not authorized"}, status = status.HTTP_403_FORBIDDEN)

    def delete(self, request, *args, **kwargs):
        if request.user.groups.filter(name = 'Manager').exists():
            return super().delete(request, *args, **kwargs)
        return Response({"message": "You are not authorized"}, status = status.HTTP_403_FORBIDDEN)
    
# User group management endpoints
@throttle_classes([OneCallPerMinute, UserRateThrottle])
class ManagersListView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name = "Manager")
    serializer_class = UserSerializer
    
    def get(self, request):
        if request.user.groups.filter(name = "Manager").exists() or request.user.is_superuser:
            return super().get(request)
        return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
    
    def post(self, request):
        if request.user.groups.filter(name = "Manager").exists() or request.user.is_superuser:
            if 'username' in request.data:
                username = request.data['username']
                user = get_object_or_404(User, username = username)
                managers = Group.objects.get(name = "Manager")
                managers.user_set.add(user)
                return Response({"message": "User added."}, status = status.HTTP_201_CREATED)
            return Response({"message": "usernamed field required"}, status = status.HTTP_400_BAD_REQUEST)
        return Response({"message": "You are not authorized"}, status = status.HTTP_403_FORBIDDEN)

@throttle_classes([OneCallPerMinute, UserRateThrottle])
class ManagerRemoveView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def delete(self, request, *args, **kwargs):
        if request.user.groups.filter(name = "Manager").exists():
            user = self.get_object()
            managers = Group.objects.get(name = "Manager")
            if user in managers.user_set.all():
                managers.user_set.remove(user)
                return Response({"message": "User removed from the Manager group."}, status=status.HTTP_200_OK)
            return Response({"message": "User not found in the Manager group."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": "You are not authorized"}, status = status.HTTP_403_FORBIDDEN) 
    
@throttle_classes([OneCallPerMinute, UserRateThrottle])
class DeliveryCrewListView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name = "Delivery crew")
    serializer_class = UserSerializer
    
    def get(self, request):
        if request.user.groups.filter(name = "Manager").exists():
            return super().get(request)
        return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
    
    def post(self, request):
        if request.user.groups.filter(name = "Manager").exists():
            if 'username' in request.data:
                username = request.data['username']
                user = get_object_or_404(User, username = username)
                managers = Group.objects.get(name = "Manager")
                managers.user_set.add(user)
                return Response({"message": "User added."}, status = status.HTTP_201_CREATED)
            return Response({"message": "usernamed field required"}, status = status.HTTP_400_BAD_REQUEST)
        return Response({"message": "You are not authorized"}, status = status.HTTP_403_FORBIDDEN)


@throttle_classes([OneCallPerMinute, UserRateThrottle])
class DeliveryCrewRemoveView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        if request.user.groups.filter(name = "Manager").exists():
            user = self.get_object()
            managers = Group.objects.get(name = "Delivery crew")
            if user in managers.user_set.all():
                managers.user_set.remove(user)
                return Response({"message": "User removed from the Delivery crew group."}, status=status.HTTP_200_OK)
            return Response({"message": "User not found in the Delivery crew group."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": "You are not authorized"}, status = status.HTTP_403_FORBIDDEN) 


# Cart management endpoints
@throttle_classes([OneCallPerMinute, UserRateThrottle])
class CartItemsView(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartItemSerializer
    
    def get(self, request):
        if request.user.is_authenticated:
            if not request.user.groups.filter(name__in = ["Manager", "Delivery crew"]).exists():
                user_cart_items = self.queryset.filter(user = request.user)
                serializer = self.serializer_class(user_cart_items, many=True)
                return Response(serializer.data)
            return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"message": "You are not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
    
    def post(self, request):
        if request.user.is_authenticated:
            if not request.user.groups.filter(name__in = ["Manager", "Delivery crew"]).exists():
                # Passing the request object to the serializer (in the context dictionary) so that
                # the serializer has access to the currently authenticated user. This allows the
                # CurrentUserDefault to work correctly and set the current user as the user for
                # the cart item being created.
                serializer = self.serializer_class(data=request.data, context =  {'request': request})
                if serializer.is_valid():
                    serializer.save(user=request.user)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"message": "You are not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.groups.filter(name__in = ["Manager", "Delivery crew"]).exists():
                user_carts = self.queryset.filter(user=request.user)
                user_carts.delete()
                return Response({"message": "Cart items deleted."}, status=status.HTTP_200_OK)
            return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"message": "You are not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)
    
# Order management endpoints
@throttle_classes([OneCallPerMinute, UserRateThrottle])
class OrdersListCreateView(generics.ListCreateAPIView):
    """
    This class defines the endpoint for retrieving and creating order and order item objects.
    """
    queryset = Order.objects.all() # Get all Order objects from the database
    serializer_class = OrderSerializer # The serializer to be used for the Order objects
    
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['user__username', 'delivery_crew__username', 'status', 'total', 'date']
    ordering_fields = ['user__username', 'delivery_crew__username', 'status', 'total', 'date']
    
    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to the endpoint.
        Returns all orders with order items based on the user's role.
        """
        # Check if the user is authenticated
        if request.user.is_authenticated:
            
            # Filters
            by_user = request.query_params.get('user')
            by_delivery_crew = request.query_params.get('delivery_crew')
            by_date = request.query_params.get('date')
            by_total = request.query_params.get('total')
                
            if by_user:
                self.queryset = self.queryset.filter(user__username = by_user)
            if by_delivery_crew:
                self.queryset = self.queryset.filter(delivery_crew__username = by_delivery_crew)
            if by_date:
                self.queryset = self.queryset.filter(date = by_date)
            if by_total:
                self.queryset = self.queryset.filter(total = by_total)
            
            # If the user is a manager
            if request.user.groups.filter(name = "Manager").exists():
                all_orders = self.queryset.all() # Get all Order objects
                all_orders = self.filter_queryset(all_orders) # Apply ordering and filtering
                serializer = self.serializer_class(all_orders, many = True) # Serialize all Order objects
                return Response(serializer.data, status = status.HTTP_200_OK) # Return serialized data
            # If the user is a delivery crew member
            elif request.user.groups.filter(name = "Delivery crew").exists():
                delivery_crew_orders = self.queryset.filter(delivery_crew = request.user) # Get Order objects assigned to the delivery crew member
                delivery_crew_orders = self.filter_queryset(delivery_crew_orders) # Apply ordering and filtering
                serializer = self.serializer_class(delivery_crew_orders, many = True) # Serialize Order objects
                return Response(serializer.data) # Return serialized data
            # If the user is a customer
            else:   
                user_orders = self.queryset.filter(user = request.user) # Get Order objects created by the user
                user_orders = self.filter_queryset(user_orders) # Apply ordering and filtering
                serializer = self.serializer_class(user_orders, many = True) # Serialize Order objects
                return Response(serializer.data) # Return serialized data
        return Response({"message": "You are not authenticated."}, status = status.HTTP_403_FORBIDDEN) # Return error message if the user is not authenticated
    
    def post(self, request):
        """
        Handle POST requests to the endpoint.
        Creates a new order and order items for the current user.
        Deletes all items from the cart for the current user.
        """
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # If the user is a customer
            if not request.user.groups.filter(name__in = ['Manager', 'Delivery crew']).exists():
                # Get current cart items for the user
                cart_items = Cart.objects.filter(user=request.user)
                # If there are items in the cart
                if cart_items.exists():
                    # Create a new Order object for the user
                    order = Order.objects.create(
                        user=request.user,
                        total=0,
                        date = date.today()
                        ) # total will be calculated and updated later
                    # Create OrderItem objects from the cart items linked to the Order object for the user
                    for item in cart_items:
                        OrderItem.objects.create(
                            order=order,
                            menuitem=item.menuitem,
                            quantity=item.quantity,
                            unit_price=item.unit_price,
                            price=item.price
                        )
                        order.total += item.price # Update the total
                    order.save()
                    cart_items.delete()
                    return Response({"message": "Order created and cart items deleted."}, status=status.HTTP_200_OK)
                return Response({"message": "No items in cart."}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"message": "You are not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
                
@permission_classes([IsAuthenticated])
@throttle_classes([OneCallPerMinute, UserRateThrottle])
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    
    # The get_object() method retrieves the instance of the model based
    # on the primary key (pk) value passed in the URL
    
    # Necessary to completely override (*args, **kwargs) the request methods because it takes
    # into account any other parameters that might be passed through URL
    # routing, such as the primary key.
    def get(self, request, *args, **kwargs):
        order = self.get_object()
        if order.user != request.user:
            return Response({"message": "Order doesnt' belong to the current user."}, status = status.HTTP_403_FORBIDDEN)
        return super().get(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        self.serializer_class = OrderSerializer
        order = self.get_object()
        if request.user.groups.filter(name = "Manager").exists():
            serializer = self.serializer_class(order, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN) 
    
    def patch(self, request, *args, **kwargs):
        self.serializer_class = OrderSerializer
        order = self.get_object()
        if request.user.groups.filter(name='Manager').exists():
            if not request.data:
                return Response({"message": "Request must contain data to update."}, status=status.HTTP_400_BAD_REQUEST)
            serializer = self.serializer_class(order, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        elif request.user.groups.filter(name = 'Delivery crew').exists():
            if not request.data:
                return Response({"message": "Request must contain data to update."}, status=status.HTTP_400_BAD_REQUEST)
            # Only allow update to status field
            if (len(request.data) == 1 and 'status' not in request.data) or (len(request.data) > 1):
                return Response({"message": "Only the status field can be updated."}, status = status.HTTP_400_BAD_REQUEST)
            serializer = self.serializer_class(order, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN) 
    
    def delete(self, request, *args, **kwargs):
        self.serializer_class = OrderSerializer
        order = self.get_object()
        if request.user.groups.filter(name = 'Manager').exists():
            self.perform_destroy(order)
            return Response({"message": "Order deleted successfully"}, status = status.HTTP_403_FORBIDDEN)
        return Response({"message": "You are not authorized"}, status = status.HTTP_403_FORBIDDEN)
        
            
# Extra views (for populating tables)
class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ['slug']
    ordering_fields = ['slug']
    search_fields = ['slug']
    
    def get(self, request):
        category = request.query_params.get('category')
        search = request.query_params.get('search')
        
        if category:
            self.queryset = self.queryset.filter(category__slug = category)
        if search:
            self.queryset = self.queryset.filter(slug__startswith = search)
        
        return super().get(request)
    
    def post(self, request):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            if request.user.groups.filter(name = "Manager").exists() or request.user.is_superuser:
                return super().post(request)
            return Response({"message": "You are not authorized"}, status = status.HTTP_403_FORBIDDEN)
        return Response({"message": "You are not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        