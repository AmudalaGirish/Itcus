from django.urls import path
from .views import employee_detail
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # API Endpoints
    path('employee/', employee_detail, name='employee_list'),
    path('employee/<int:emp_id>/', employee_detail, name='employee_detail'),

    # auth token Endpoints
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
