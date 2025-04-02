from django.urls import path, include

from .views.accountView import AccountListView, AccountCreateView, AccountDetailView
from .views.journalDetailsView import JournalDetailsDetailView, JournalDetailsCreateView, JournalDetailsListView
from .views.journalView import JournalListView, JournalCreateView, JournalDetailView
from .views.partyView import PartyListView, PartyCreateView, PartyDetailView
from .views.transactionsView import TransactionsListView, TransactionsDetailView, TransactionsCreateView
from .views.userView import UserCreateView, UserListView, UserDetailView
from .views.subscriberView import SubscriberListView, SubscriberCreateView, SubscriberDetailView

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('users/create/', UserCreateView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('subscribers/', SubscriberListView.as_view()),
    path('subscribers/create/', SubscriberCreateView.as_view()),
    path('subscribers/<int:pk>/', SubscriberDetailView.as_view()),
    path('accounts/', AccountListView.as_view()),
    path('accounts/create/', AccountCreateView.as_view()),
    path('accounts/<int:pk>/', AccountDetailView.as_view()),
    path('journals/', JournalListView.as_view()),
    path('journals/create/', JournalCreateView.as_view()),
    path('journals/<int:pk>/', JournalDetailView.as_view()),
    path('journalDetails/', JournalDetailsListView.as_view()),
    path('journalDetails/create/', JournalDetailsCreateView.as_view()),
    path('journalDetails/<int:pk>/', JournalDetailsDetailView.as_view()),
    path('parties/', PartyListView.as_view()),
    path('parties/create/', PartyCreateView.as_view()),
    path('parties/<int:pk>/', PartyDetailView.as_view()),
    path('transactions/', TransactionsListView.as_view()),
    path('transactions/create', TransactionsCreateView.as_view()),
    path('transactions/<int:pk>/', TransactionsDetailView.as_view()),


]