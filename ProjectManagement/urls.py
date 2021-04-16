from django.urls import path
from . import views

urlpatterns = [

        # path('mail',views.index),

         path('BO/',views.BOListView.as_view(),name='details'),
        path('BO/<pk>/',views.BOView.as_view(),name='put'),
         path('Project/',views.ProjectListView.as_view(),name='details'),
        path('Project/<pk>/',views.ProjectView.as_view(),name='put'),
         #path('Team/',views.TeamListView.as_view(),name='details'),

    # path('Team/<name>/edit/',views.TeamUpdateAPIView.as_view(),name='put'),

        #path('',views.ProjectManagement,name='project')
        
]
