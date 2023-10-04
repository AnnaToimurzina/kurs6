from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
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

@method_decorator(login_required, name='dispatch')
class ClientListView(ListView, LoginRequiredMixin):
    model = Client
    template_name = 'rassilki/client_list.html'

    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        context['title'] = 'Клиенты'
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser or user.is_staff:
                queryset = super().get_queryset()
            else:
                queryset = super().get_queryset().filter(
                    client_owner=user.pk
                )
        else:
            queryset = super().get_queryset().filter(
                pk=None
            )
        return queryset

class ClientUpdateView(UpdateView, LoginRequiredMixin):
    model = Client
    form_class = ClientForm
    template_name = 'rassilki/client_form.html'

    def get_context_data(self, **kwargs):
        context = super(ClientUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Edit Clients'
        return context

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.client_owner != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object

class ClientDetailView(DetailView, LoginRequiredMixin):
    model = Client
    template_name = 'rassilki/client_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ClientDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Clients Details'
        return context


class ClientDeleteView(DeleteView, LoginRequiredMixin):
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
    template_name = 'rassilki/create_mailing.html'
    form_class = MailingMessageForm
    success_url = reverse_lazy('rassilki:home')

    def get_context_data(self, **kwargs):
        context = super(MailingCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Mailing Campaign Creation'
        return context

    def get_success_url(self):
        return reverse('rassilki:mailing-detail', args=[self.object.pk])

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.mail_owner = self.request.user
        self.object.save()
        return redirect(self.get_success_url())

@method_decorator(login_required, name='dispatch')
class MailingListView(ListView, LoginRequiredMixin):
    model = MailingMessage
    template_name = 'rassilki/mailing-list.html'

    def get_context_data(self, **kwargs):
        context = super(MailingListView, self).get_context_data(**kwargs)
        context['title'] = 'Mailing Campaigns'
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            queryset = super().get_queryset()
        else:
            queryset = super().get_queryset().filter(
                mail_owner=user.pk
            )
        return queryset

class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingMessage
    form_class = MailingMessageForm
    template_name = 'rassilki/create_mailing.html'

    def get_context_data(self, **kwargs):
        context = super(MailingUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Edit Campaign'
        return context

    def get_success_url(self):
        return reverse('rassilki:mailing-detail', args=[self.object.pk])



class MailingDetailView(DetailView, LoginRequiredMixin):
    model = MailingMessage
    template_name = 'rassilki/mailing_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MailingDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Campaign Details'
        return context


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingMessage
    template_name = 'rassilki/mailing_confirm_delete.html'
    success_url = reverse_lazy('rassilki:mailing-list')

    def get_context_data(self, **kwargs):
        context = super(MailingDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Delete Campaign'
        return context
















