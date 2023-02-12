# Little Lemon API Project
This project showcases the development of back-end APIs for the Little Lemon restaurant as part of the Meta Backend Developer Certificate program. The APIs provide functionalities such as user management, menu management, order management, and customer interactions.

# Features
* User authentication (Admin, Manager, Delivery Crew, and Customer)
* Menu browsing and management
* Cart management
* Order placement and management
* Delivery management

# Rubric
## Test if the admin can assign users to the manager group:
Make a POST call to this endpoint http://127.0.0.1:8000/api/groups/manager/users with a valid admin token and a valid username in the HTTP REQUEST body. 
![Test_if_the_admin_can_assign_users_to_the_manager_group](Rubric_test_images/Test_if_the_admin_can_assign_users_to_the_manager_group.png)

##  Test if you can access the manager group with an admin token:         
Make a GET call to http://127.0.0.1:8000/api/groups/manager/users with an admin token. 
![Test if you can access the manager group with an admin token](Rubric_test_images/Test_if_you_can_access_the_manager_group_with_an_admin_token.png)

## Test if the admin can add menu items:
Make a POST call to this endpoint http://127.0.0.1:8000/api/menu-items with the admin token and necessary data. Or, log into the Django admin panel as super admin and then browse this endpoint in your browser and add some menu items. 
![Test_if_the_admin_can_add_menu_items](Rubric_test_images/Test_if_the_admin_can_add_menu_items.png)
![Test_if_the_admin_can_add_menu_items](Rubric_test_images/Test_if_the_admin_can_add_menu_items(2).png)

## Test if the admin can add categories:
Make a POST call to this endpoint http://127.0.0.1:8000/api/categories with the admin token and necessary data. Or log into the Django admin panel as super admin and then browse this endpoint in your browser and add some menu items.
![Test_if_the_admin_can_add_categories](Rubric_test_images/Test_if_the_admin_can_add_categories.png)

## Test if the manager can log in:
Make a POST call to this endpoint http://127.0.0.1:8000/auth/token/login/ with the username and password of a manager.
![Test_if_the_manager_can_log_in](Rubric_test_images/Test_if_the_manager_can_log_in.png)

## Test if the manager can update the item of the day:
Make a PATCH call to the endpoint of any single menu item endpoint like this http://127.0.0.1:8000/api/menu-items/1 with a manager token. Add a featured field in the REQUEST body with its value set to true or false. 
![Test_if_the_manager_can_update_the_item_of_the_day](Rubric_test_images/Test_if_the_manager_can_update_the_item_of_the_day.png)

## Test if the manager can assign users to the delivery crew:
Make a POST call to this endpoint http://127.0.0.1:8000/api/groups/manager/users with a valid manager token and a valid username in the HTTP REQUEST body. 
![Test_if_the_manager_can_assign_users_to_the_delivery_crew](Rubric_test_images/Test_if_the_manager_can_assign_users_to_the_delivery_crew.png)

## Test if the manager can assign orders to the delivery crew:
Make a PATCH call to an endpoint of any single order item like this http://127.0.0.1:8000/api/orders/1  with a manager token. Add a delivery_crew field in the REQUEST body with its value set to any delivery crew user id.
![Test_if_the_manager_can_assign_orders_to_the_delivery_crew](Rubric_test_images/Test_if_the_manager_can_assign_orders_to_the_delivery_crew.png)

## Test if the delivery crew can view orders assigned to them:
Make a GET call to this endpoint http://127.0.0.1:8000/api/orders with a delivery crew token.
![Test_if_the_delivery_crew_can_view_orders_assigned_to_them](Rubric_test_images/Test_if_the_delivery_crew_can_view_orders_assigned_to_them.png)

## Test if the delivery crew can update an order as delivered:
Make a PATCH call to this endpoint to any single order item endpoint like this http://127.0.0.1:8000/api/orders/1  with a delivery crew token. Add a status field in the REQUEST body with its value set to true or false.
![Test_if_the_delivery_crew_can_update_an_order_as_delivered](Rubric_test_images/Test_if_the_delivery_crew_can_update_an_order_as_delivered.png)

## Test if customers can register:
Make a POST call to this endpoint http://127.0.0.1:8000/auth/users/ with a username, password and email in the HTTP REQUEST body.
![Test_if_customers_can_register](Rubric_test_images/Test_if_customers_can_register.png)

## Test if customers can log in using their username and password and get access tokens:
Make a POST call to this endpoint http://127.0.0.1:8000/auth/token/login/ with a valid username and password in the HTTP Request body.    
![Test_if_customers_can_log_in_using_their_username_and_password_and_get_access_tokens](Rubric_test_images/Test_if_customers_can_log_in_using_their_username_and_password_and_get_access_tokens.png)

## Test if customers can browse all categories:
Make a GET API call to this endpoint http://127.0.0.1/api/categories with a customer token
![Test_if_customers_can_browse_all_categories](Rubric_test_images/Test_if_customers_can_browse_all_categories.png)

## Test if customers can browse all menu items:
Make a GET API call to this endpoint http://127.0.0.1/api/menu-items with a customer token
![Test_if_customers_can_browse_all_menu_items](Rubric_test_images/Test_if_customers_can_browse_all_menu_items.png)

## Test if customers can browse menu items by category:
Make a GET API call to these endpoints, http://127.0.0.1:8000/api/menu-items?search=Icecream or any available category name instead of Icecream with a customer token.
![Test_if_customers_can_browse_menu_items_by_category](Rubric_test_images/Test_if_customers_can_browse_menu_items_by_category.png)

## Test if customers can paginate menu items:
Make a GET API call to the endpoints http://127.0.0.1:8000/api/menu-items?page=1 or http://127.0.0.1:8000/api/menu-items?page=2 with a customer token.
![Test_if_customers_can_paginate_menu_items(page1)](Rubric_test_images/Test_if_customers_can_paginate_menu_items(page1).png)
![Test_if_customers_can_paginate_menu_items(page2)](Rubric_test_images/Test_if_customers_can_paginate_menu_items(page2).png)

## Test if customers can sort menu items by price:
Make a GET API call to the endpoint http://127.0.0.1:8000/api/menu-items?ordering=price or http://127.0.0.1:8000/api/menu-items?ordering=-price with a customer token.
![Test_if_customers_can_sort_menu_items_by_price(ascending)](Rubric_test_images/Test_if_customers_can_sort_menu_items_by_price(ascending).png)
![Test_if_customers_can_sort_menu_items_by_price(descending)](Rubric_test_images/Test_if_customers_can_sort_menu_items_by_price(descending).png)

## Test if customers can add menu items to the cart:
Make a POST call to this endpoint http://127.0.0.1:8000/api/cart/menu-items with a customer token. Add these fields with valid data in the REQUEST body for menuitem, unit_price, quantity.
![Test_if_customers_can_add_menu_items_to_the_cart](Rubric_test_images/Test_if_customers_can_add_menu_items_to_the_cart.png)

## Test if customers can see previously added items in the cart:
Make a GET call to this endpoint http://127.0.0.1:8000/api/cart/menu-items with a customer token. 
![Test_if_customers_can_see_previously_added_items_in_the_cart](Rubric_test_images/Test_if_customers_can_see_previously_added_items_in_the_cart.png)

## Test if customers can place orders:
Make a POST call to this endpoint http://127.0.0.1:8000/api/cart/orders with a customer token. Add only the date field with valid data in the REQUEST body. Here is a sample date – 2022-11-16.
![Test_if_customers_can_place_orders](Rubric_test_images/Test_if_customers_can_place_orders.png)

## Customers can view their own orders:
Make a GET call to this endpoint http://127.0.0.1:8000/api/cart/orders with a customer token. 
![Customers_can_view_their_own_orders](Rubric_test_images/Customers_can_view_their_own_orders.png)
















