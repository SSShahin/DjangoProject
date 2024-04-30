from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from emp import views

urlpatterns = [
   path('',views.home,name='home'),
   path('addemp',views.add_emp,name='add_emp'),
   path('delete<int:emp_id>',views.delete,name='delete'),
   path('update<int:emp_id>',views.update,name='update'),
   path('<int:emp_id>',views.do_update,name='updatedata'),
   path('testimonial',views.test,name='testimonial'),
   path('feedback',views.feedback,name='feedback')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)