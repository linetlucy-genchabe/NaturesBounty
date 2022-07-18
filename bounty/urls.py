from django.urls import  re_path as url, include,path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'register/$',views.register ),
    url(r'accounts/login/$',views.user_login, name='login'),
    url(r'logout/$',views.signout),
    url(r'^accounts/profile/$', views.user_profiles, name='profile'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^single/post/(\d+)$', views.single_post, name='single_post'),
    url(r'^search/', views.search_posts, name='search_results'),
    

    path('contact',views.contact, name = 'contact'),
    path('cart',views.cart, name ='cart'),
    path('updatecart',views.updateCart),
    path('updatequantity',views.updateQuantity),
    path('checkout', views.checkout, name = 'checkout'),
  
   
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)