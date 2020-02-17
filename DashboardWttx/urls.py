"""DashboardWttx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import wttxApp.views as test_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", include('chartProject.urls'))
# ]

urlpatterns = [
    path('wttx/', test_views.wttx, name='wttx'),
    path('chart1/', test_views.wttx, name='chart1'),
    path('chart2/', test_views.wttx, name='chart2'),
]
