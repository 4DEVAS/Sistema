from django.contrib import admin
from django.urls import path
from app.views import home, home_produto, produto_novo, produto_create, index, form, create, view, edit, update, delete, produto_view, produto_update, produto_delete, produto_edit

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('home_produto/', home_produto, name='home_produto'),
    path('produto/novo/', produto_novo, name='produto_novo'),
    path('produto/create/', produto_create, name='produto_create'),
    path('produto_view/<int:pk>/', produto_view, name='produto_view'),
    path('produto/update/<int:pk>/', produto_update, name='produto_update'),
    path('produto_edit/<int:pk>/', produto_edit, name='produto_edit'),
    path('produto_delete/<int:pk>/', produto_delete, name='produto_delete'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
]