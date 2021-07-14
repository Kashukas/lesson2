from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from . import forms, models
from django.contrib import messages
import comments

# Create your views here.

class CommentCreateView(FormView):
    form_class = forms.CommentCreateForm

    def form_valid(self, form):
        next_page = form.cleaned_data.get('next_page')
        comment_text = form.cleaned_data.get('comment_text')
        author = self.request.user
        content_type_id = form.cleaned_data.get('content_type_id')
        content_type = ContentType.objects.get_for_id(content_type_id)
        object_id = form.cleaned_data.get('object_id')
        try:
            comment = models.Comment.objects.create(
                author=author,
                comment_text=comment_text,
                content_type=content_type,
                object_id=object_id
                )
            return HttpResponseRedirect(next_page)
        except ValueError:
            messages.add_message(
            self.request, messages.WARNING, 
            f'{str(self.request.user)}, ваш комментарий не отправлен. Возможно, вам нужно зарегистрироваться или авторизоваться.'
            )
            return HttpResponseRedirect(next_page)