from django.urls import path
#from django.conf.urls import url
from . import views
app_name = 'notes'
urlpatterns = [
    path ('',views.index , name = 'index'),
    path ('<int:note_id>',views.detail , name = 'detail'),
    path ('add/',views.add , name = 'add'),
    path ('<int:note_id>/edit',views.edit , name = 'edit'),
    path ('<int:note_id>/delete',views.delete , name = 'delete')

]
