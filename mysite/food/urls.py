from django.urls import path
from . import views


urlpatterns = [
    #/food
    path('', views.IndecClassView.as_view(), name='index'),
    #/food/1
    # path('<int:item_id>/', views.detail, name='detail'), # function based url
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'), #class based url

    path('item/', views.item, name='item'),

    # add  items
    # path('add', views.create_item, name='create_item'),
    path('add', views.CreateItem.as_view(), name='create_item'),

    # edit items
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),

    # delete items
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),

    # Search and pagination for food items
    # path('food-list/', views.food_list, name='food_list'),

]