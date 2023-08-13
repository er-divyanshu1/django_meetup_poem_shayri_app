from django.contrib import admin
from django.urls import include, path
from app1 import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('category/<slug:url>',views.category,name="category"),
    path('about_us',views.about_us,name="about_us"),
    path('term_condition',views.term_condition,name="term_condition"),
    path('contact_us',views.contact_us,name="contact_us"),
    

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)