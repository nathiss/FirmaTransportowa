from django.urls import path

from . import views


app_name = 'webapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),

    path('user/change_password', views.ChangePasswordView.as_view(), name='change_password'),
    path('user/buy_ticket', views.CreateTicketView.as_view(), name='create_ticket'),

    path('staff/create_post', views.CreatePostView.as_view(), name='create_post'),
    path('staff/delete_post/<uuid:post_id>', views.DeletePostView.as_view(), name='delete_post'),
    path('staff/edit_post/<uuid:post_id>', views.EditPostView.as_view(), name='edit_post'),

    path('staff/create_place', views.CreatePlaceView.as_view(), name='create_place'),
    path('staff/create_connection', views.CreateConnectionView.as_view(), name='create_connection'),

    path('about_us', views.about_us, name='about_us'),
    path('contact', views.contact, name='contact'),
]
