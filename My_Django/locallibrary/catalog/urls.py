from django.conf.urls import include,url
from . import views
urlpatterns = [
    url('',views.index,name='index'),
    url('books/', views.BookListView.as_view(), name='books'),
    url('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]