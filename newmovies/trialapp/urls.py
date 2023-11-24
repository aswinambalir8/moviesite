from django.conf.urls.static import static
from django.urls import path

from newmovies import settings
from .import views
app_name = 'movieapp'

urlpatterns = [

    path('',views.data,name='data'),
    path('movie/<int:uniq_id>/',views.main,name='main'),
    path('add/',views.insert,name='insert'),
    path('update/<int:uid>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)