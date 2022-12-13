from .models import Tag


class ContextDataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        tags = Tag.objects.all()
        context['tags'] = tags
        return context
