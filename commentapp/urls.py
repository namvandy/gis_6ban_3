
from django.contrib import admin
from django.urls import path, include

from commentapp.views import CommentCreateView, CommentDeleteView

app_name = 'commentapp'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('create/', CommentCreateView.as_view(), name='create'),
    path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),
]
