from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.shortcuts import redirect


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Inicio"
        return context


class SigninView(LoginView):
    template_name = 'login/signin.html'
    redirect_field_name = None
    redirect_authenticated_user = reverse_lazy('index')

    def get_form(self):
        form = super().get_form()
        form.fields['username'].widget.attrs.update(
            {'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
        form.fields['password'].widget.attrs.update(
            {'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Iniciar Sesión"
        return context


class SignupView(FormView):
    template_name = 'login/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('signin')

    def get_form(self):
        form = super().get_form()
        form.fields['username'].widget.attrs.update(
            {'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
        form.fields['password1'].widget.attrs.update(
            {'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
        form.fields['password2'].widget.attrs.update(
            {'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrarse"
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LogoutView(LogoutView):
    next_page = 'index'
