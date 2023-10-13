from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('signup', SignupView.as_view(), name='signup'),
    path('subscribe', AddPackagesToUserView.as_view(), name='subscribe'),
    path('subscriptions', SubscriptionsView.as_view(), name='subscriptions'),

]
