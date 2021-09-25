from django.urls import path
from .views import (
    MessageListView,
    LanguageCreateView,
    MessageCreateView
)
from . import views

urlpatterns = [
	path('', MessageListView.as_view(), name='messages-home'),
	path('language/', LanguageCreateView.as_view(), name='language-create'),
	path('message/new/', MessageCreateView.as_view(), name='message-create'),
	
]