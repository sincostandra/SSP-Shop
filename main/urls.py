from django.urls import include, path
from main.views import logout, show_main, create_product, edit_product, delete_product, create_product_ajax
from main.views import show_main, create_product, show_xml, show_json, create_product_flutter
from main.views import show_xml_by_id, show_json_by_id, register, login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name = 'delete_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-product-ajax', create_product_ajax, name='create_product_ajax'),
    path('auth/', include('authentication.urls')),
    path('create-flutter/', create_product_flutter, name='create_mood_flutter'),
    path('logout/', logout, name='logout'),
]