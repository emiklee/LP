from .models import *


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['cats'] = cats
        if 'category_selected' not in context:
            context['category_selected'] = 0
        return context
