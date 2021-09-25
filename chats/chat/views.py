from django.shortcuts import render
from .models import Message, Language
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from google_trans_new import google_translator




# Create your views here.


def home(request):
    context = {
        'doubts': Doubt.objects.all(),
        'colors': ['bg-dark', 'bg-danger'],
        'from_date': timezone.now()
    }
    return render(request, 'chat/index.html', context)




def hinglish(sent,dest="mr"):### src means lang code of sender and dest means lang code for receivers...
    translator = google_translator()
    result = translator.translate(sent,lang_tgt=dest)
    return result

class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'chat/index.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['colors'] = ['bg-dark', 'bg-danger']
        context['messagess'] = Message.objects.all()
        for i in context['messagess']:
            a = hinglish(i, self.request.user.language.language)
            i.translated = a
        

        print(self.request.user.language.language)
        # print(context['messages'])
        return context

class LanguageCreateView(LoginRequiredMixin, CreateView):
    model = Language
    fields = ['language']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['content']

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)








