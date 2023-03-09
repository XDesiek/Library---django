from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'book'

urlpatterns = [
    # # path('<int:id>/', views.book_detail, name='book_detail')
    # path("", views.BookListView.as_view(), name="book_list"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.book_list, name='book_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:book>/',views.book_detail,name="book_detail",),
    path('<int:book_id>/share/',views.book_share, name='book_share'),
    path('<int:book_id>/comment/', views.book_comment, name='book_comment'),
    path('tag/<slug:tag_slug>/',views.book_list, name='book_list_by_tag'),
    #    path('', views.dashboard, name='dashboard'),
    # path("createuser",views.create_user,name ="createuser")
    # path("login",views.login,name='login'),

]


