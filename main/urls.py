from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user, increment_item, decrement_item, delete_item
from main.views import edit_item, get_item_ajax, create_ajax, delete_item_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increment_item/<str:id>/', increment_item, name='increment_item'),
    path('decrement_item/<str:id>/', decrement_item, name='decrement_item'),
    path('delete_item/<str:id>', delete_item, name='delete_item'),
    path('edit-item/<str:id>', edit_item, name='edit_item'),
    path('get-item/', get_item_ajax, name='get_item_ajax'),
    path('create_ajax/', create_ajax, name='create_ajax'),
    path('delete-item-ajax/<str:id>/', delete_item_ajax, name='delete_item_ajax'),
]