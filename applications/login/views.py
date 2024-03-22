from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
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
    redirect_authenticated_user = reverse_lazy('index')
    input_class_name = ("block w-full rounded-md border-0 bg-gray-900 py-1.5 "
                        "text-white shadow-sm ring-1 ring-inset ring-white/10 "
                        "focus:ring-2 focus:ring-inset focus:ring-indigo-500 "
                        "sm:text-sm sm:leading-6")

    def get_form(self):
        form = super().get_form()
        for field in form.fields:
            form.fields[field].widget.attrs.update(
                {'class': self.input_class_name})
        form.fields['username'].label = _('Usuario o correo')
        form.fields['password'].label = _('Contraseña')
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Iniciar Sesión"
        return context
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Usuario o contraseña incorrectos')
        return response


class SignupView(FormView):
    template_name = 'login/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('signin')
    input_class_name = ("block w-full rounded-md border-0 bg-gray-900 py-1.5 "
                        "text-white shadow-sm ring-1 ring-inset ring-white/10 "
                        "focus:ring-2 focus:ring-inset focus:ring-indigo-500 "
                        "sm:text-sm sm:leading-6")

    def get_form(self):
        form = super().get_form()
        for field in form.fields:
            form.fields[field].widget.attrs.update(
                {'class': self.input_class_name})
        form.fields['password1'].label = _('Contraseña')
        form.fields['password2'].label = _('Confirmar contraseña')
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrarse"
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class SignOutView(LogoutView):
    next = 'index'
