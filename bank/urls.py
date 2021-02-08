from django.urls import path

from bank.views import home,acc,login,usr,balanceEnq,transfer,deposit,withdraw

urlpatterns = [
    path('home/',home,name='home'),
    path('create/',acc,name='create'),
    path('login/',login,name='login'),
    path('user/',usr,name='user'),
    path('balance/',balanceEnq,name='balance'),
    path('transfer/',transfer,name='transfer'), 
    path('deposit/',deposit,name='deposit'),
    path('withdraw/',withdraw,name='withdraw')  

    ]   