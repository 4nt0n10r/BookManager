from django.forms.widgets import DateInput
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Book, Author, Gender


class BookListView(ListView):
    template_name = 'bookmanager/books/index.html'
    model = Book
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Lista de Libros"
        return context

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)


class BookCreateView(CreateView):
    template_name = 'bookmanager/books/create.html'
    model = Book
    fields = ['title', 'author', 'gender']
    success_url = reverse_lazy('books')

    def get_form(self):
        form = super().get_form()
        form.fields['title'].widget.attrs.update(
            {'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
        form.fields['author'].widget.attrs.update(
            {'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
        form.fields['gender'].widget.attrs.update(
            {'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class BookUpdateView(UpdateView):
    template_name = 'bookmanager/books/create.html'
    model = Book
    fields = ['title', 'author', 'gender']
    success_url = reverse_lazy('books')

    def get_form(self):
        form = super().get_form()
        form.fields['title'].widget.attrs.update(
            {'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
        form.fields['author'].widget.attrs.update(
            {'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
        form.fields['gender'].widget.attrs.update(
            {'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('books')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class AuthorListView(ListView):
    template_name = 'bookmanager/authors/index.html'
    model = Author
    context_object_name = 'authors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Lista de Autores"
        return context

    def get_queryset(self):
        return Author.objects.filter(user=self.request.user)


class AuthorCreateView(CreateView):
    template_name = 'bookmanager/authors/create.html'
    model = Author
    fields = ['name', 'birth_date']
    success_url = reverse_lazy('authors')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget.attrs.update(
            {'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
        form.fields['birth_date'].widget.attrs.update(
            {'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
        return form


class AuthorUpdateView(UpdateView):
    template_name = 'bookmanager/authors/create.html'
    model = Author
    fields = ['name', 'birth_date']
    success_url = reverse_lazy('authors')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget.attrs.update(
            {'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
        form.fields['birth_date'].widget.attrs.update(
            {'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
        return form


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class GenderListView(ListView):
    template_name = 'bookmanager/genders/index.html'
    model = Gender
    context_object_name = 'genders'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Lista de Géneros"
        return context

    def get_queryset(self):
        return Gender.objects.filter(user=self.request.user)


class GenderCreateView(CreateView):
    template_name = 'bookmanager/genders/create.html'
    model = Gender
    fields = ['name']
    success_url = reverse_lazy('genders')

    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget.attrs.update(
            {'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class GenderUpdateView(UpdateView):
    template_name = 'bookmanager/genders/create.html'
    model = Gender
    fields = ['name']
    success_url = reverse_lazy('genders')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Lista de Géneros"
        return context

    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget.attrs.update(
            {'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GenderDeleteView(DeleteView):
    model = Gender
    success_url = reverse_lazy('genders')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
