from django.core.cache import cache

from .models import Tag


class ContextDataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        # добавление кэширования по ключу
        tags = cache.get('tags')
        if not tags:
            tags = Tag.objects.all()
            cache.set('tags', tags, 60)
        context['tags'] = tags
        return context
