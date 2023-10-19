from django.urls import path

from rassilki.apps import RassilkiConfig
from rassilki.views import HomePageView, ClientCreateView, MailingCreateView, ClientDetailView, ClientUpdateView, \
    ClientDeleteView, contacts, ClientListView, MailingListView, MailingDetailView, MailingUpdateView, \
    MailingDeleteView, index

app_name = RassilkiConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('', index, name='index'),
    path('client_form/', ClientCreateView.as_view(), name='client-create'),
    path('client/', ClientListView.as_view(), name='client-list'),
    path('client/<int:pk>/detail/', ClientDetailView.as_view(), name='client-detail'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client-update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),

    path('contacts/', contacts, name='contacts'),

    path('create_mailing/', MailingCreateView.as_view(), name='mailing-create'),
    path('mailing/', MailingListView.as_view(), name='mailing-list'),
    path('mailing/<int:pk>/detail/', MailingDetailView.as_view(), name='mailing-detail'),
    path('mailing/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing-update'),
    path('mailing/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing-delete'),

]
