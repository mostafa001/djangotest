"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from stockmanagement.views import home_view, list_items, add_items, delete_items, update_items, sell_items, sales_history
from account.views import login_view, logout_view
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('api/list_items/', list_items, name='list_items'),
    path('api/add_items/', add_items, name='add_items'),
    path('api/delete_items/<str:id>/', delete_items, name="delete_items"),
    path('api/update_items/<str:id>/', update_items, name="update_items"),
    path('api/sell_items/<str:id>/', sell_items, name="sell_items"),
    path('api/sales_history/<str:id>/', sales_history, name="sales_history"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
