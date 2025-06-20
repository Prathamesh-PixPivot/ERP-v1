from django.urls import path

from .views import register_view, me_view, register_organization, list_organizations, \
    login_jwt_view, logout_jwt_view, TenantTokenRefreshView

urlpatterns = [
    path('organization/register/', register_organization, name='register-org'),
    path('organization/list/', list_organizations, name='list-orgs'),
    path('register/', register_view, name='register'),
    path('me/', me_view, name='me'),
    path('login/', login_jwt_view, name='jwt_login'),
    path('logout/', logout_jwt_view, name='jwt_logout'),
    path('token/refresh/', TenantTokenRefreshView.as_view(), name='token_refresh'),
]
