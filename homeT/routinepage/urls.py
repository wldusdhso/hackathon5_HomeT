from django.urls import path
from . import views

app_name='routinepage'

urlpatterns = [ 
    path('',views.home,name='home'),
    path('new',views.new,name='new'),
    path('postcreate',views.postcreate,name='postcreate'),
    path('detail/<int:post_id>',views.detail, name="detail"),
    path('postedit/<int:post_id>',views.postedit, name="postedit"),
    path('postupdate/<int:post_id>',views.postupdate, name="postupdate"),
    path('postdelete/<int:post_id>',views.postdelete, name="postdelete"),
    path('commentcreate/<int:post_id>',views.commentcreate,name='commentcreate'),
    path('commentdelete/<int:post_id>/<int:comment_id>',views.commentdelete,name='commentdelete'),
]
    