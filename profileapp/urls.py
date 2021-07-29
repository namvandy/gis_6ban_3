from django.urls import path

from profileapp.views import ProfileCreationView, ProfileUpdateView

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreationView.as_view(), name="create"),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name="update"),
]

