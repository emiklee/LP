from django.http import HttpResponse, HttpResponseNotFound, HttpRequest
from django.shortcuts import render, get_object_or_404
from .models import *
from .utils import *
from django.views.generic import ListView, DeleteView, CreateView, FormView


class KafeHome(DataMixin, ListView):
    model = Product
    template_name = 'kafe/index.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


class KafeMenu(DataMixin, ListView):
    model = Product
    template_name = 'kafe/menu.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Меню')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Product.objects.filter(available=True).select_related('category')


class Kafe_About(DataMixin, ListView):
    model = Product
    template_name = 'kafe/about.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='О нас')
        return dict(list(context.items()) + list(c_def.items()))


class Kafe_Delivery(DataMixin, ListView):
    model = Product
    template_name = 'kafe/delivery.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Доставка и оплата')
        return dict(list(context.items()) + list(c_def.items()))


class KafeContact(DataMixin, ListView):
    model = Product
    template_name = 'kafe/contact.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Контакты')
        return dict(list(context.items()) + list(c_def.items()))


class KafeCategory(DataMixin, ListView):
    model = Product
    template_name = 'kafe/menu.html'
    context_object_name = 'products'
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'], available=True).select_related(
            'category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['category_slug'])
        c_def = self.get_user_context(title='Категория -' + str(c.name),
                                      category_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


class KafePost(DataMixin, ListView):
    model = Product
    template_name = 'kafe/menu.html'
    slug_url_kwarg = 'products_slug'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(slug=self.kwargs['products_slug'])

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['products'])
        return dict(list(context.items()) + list(c_def.items()))


def PageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
