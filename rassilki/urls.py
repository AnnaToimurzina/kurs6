from django.urls import path

from rassilki.apps import RassilkiConfig
from rassilki.views import HomePageView, ClientCreateView, MailingCreateView

app_name=RassilkiConfig.name



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('client_form/', ClientCreateView.as_view(), name='create'),
    path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),

    ]