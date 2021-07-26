from django.urls import path

from profileapp.views import ProfileCreationView

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreationView.as_view(), name="create"),

]

