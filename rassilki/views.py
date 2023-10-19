from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import Http404
from .forms import ClientForm, MailingMessageForm
from .models import Client, MailingMessage


class HomePageView(ListView):
    model = Client
    template_name = 'rassilki/home.html'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('rassilki:home')

    def get_context_data(self, **kwargs):
        context = super(ClientCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Новый клиент'
        return context

    def get_success_url(self):
        return reverse('rassilki:client-detail', args=[self.object.pk])

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.client_owner = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class ClientListView(ListView):
    model = Client
    template_name = 'rassilki/client_list.html'

    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        context['title'] = 'Клиенты'
        return context

    def get_queryset(self):
        return super().get_queryset()


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'rassilki/client_form.html'

    def get_context_data(self, **kwargs):
        context = super(ClientUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Edit Clients'
        return context

    def get_success_url(self):
        return reverse('rassilki:client-detail', args=[self.object.pk])


class ClientDetailView(DetailView):
    model = Client
    template_name = 'rassilki/client_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ClientDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Clients Details'
        return context


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'rassilki/client_confirm_delete.html'
    success_url = reverse_lazy('rassilki:client-list')

    def get_context_data(self, **kwargs):
        context = super(ClientDeleteView, self).get_context_data()
        context['title'] = 'Delete Client'
        return context


def contacts(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        subject = requests.POST.get('subject')
        message = requests.POST.get('message')

    context = {
        'title': 'Contact Us',
    }

    return render(requests, 'rassilki/contacts.html', context)


class MailingCreateView(CreateView):
    model = MailingMessage
    form_class = MailingMessageForm
    template_name = 'rassilki/create_mailing.html'

    def get_success_url(self):
        return reverse('rassilki:mailing-detail', args=[self.object.pk])


class MailingListView(ListView):
    model = MailingMessage
    template_name = 'rassilki/mailing_list.html'

    def get_queryset(self):
        return super().get_queryset()


class MailingUpdateView(UpdateView):
    model = MailingMessage
    form_class = MailingMessageForm
    template_name = 'rassilki/create_mailing.html'

    def get_success_url(self):
        return reverse('rassilki:mailing-detail', args=[self.object.pk])


class MailingDetailView(DetailView):
    model = MailingMessage
    template_name = 'rassilki/mailing_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MailingDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Campaign Details'
        return context


class MailingDeleteView(DeleteView):
    model = MailingMessage
    template_name = 'rassilki/mailing_confirm_delete.html'
    success_url = reverse_lazy('rassilki:mailing-list')

    def get_context_data(self, **kwargs):
        context = super(MailingDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Delete Campaign'
        return context


def index(request):
    return render(request, 'rassilki/index.html')
