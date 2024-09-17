from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name = 'index.html')),

    path('index/',TemplateView.as_view(template_name = 'index.html'),name='index'),
    path('category/',TemplateView.as_view(template_name = 'category.html'),name='category'),
    path('single-product/',TemplateView.as_view(template_name = 'single-product.html'),name='single-product'),
    path('checkout/',TemplateView.as_view(template_name = 'checkout.html'),name='checkout'),
    path('cart/',TemplateView.as_view(template_name = 'cart.html'),name='cart'),
    path('confirmation/',TemplateView.as_view(template_name = 'confirmation.html'),name='confirmation'),
    path('blog/',TemplateView.as_view(template_name = 'blog.html'),name='blog'),
    path('single-blog/',TemplateView.as_view(template_name = 'single-blog.html'),name='single-blog'),
    path('login/',TemplateView.as_view(template_name = 'login.html'),name='login'),
    path('tracking/',TemplateView.as_view(template_name = 'tracking.html'),name='tracking'),
    path('elements/',TemplateView.as_view(template_name = 'elements.html'),name='elements'),
    path('contact/',TemplateView.as_view(template_name = 'contact.html'),name='contact'),

    path('product/',include('product.urls'))

]
