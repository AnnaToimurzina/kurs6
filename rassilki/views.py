from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ClientForm, MailingMessageForm
from .models import Client, MailingMessage


class HomePageView(ListView):
    model = Client
    template_name = 'rassilki/home.html'

class ClientCreateView(CreateView):
  model = Client
  form_class = ClientForm
  success_url = reverse_lazy('rassilki:home')

class MailingCreateView(CreateView):
    model = MailingMessage
    template_name = 'rassilki/create_mailing.html'
    form_class = MailingMessageForm
    success_url = reverse_lazy('rassilki:home')


















