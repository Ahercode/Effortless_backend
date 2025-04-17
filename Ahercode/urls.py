from django.urls import path, include

from .views.accountDetailsView import AccountDetailView, AccountDetailListView, AccountDetailCreateView
from .views.accountView import AccountListView, AccountCreateView, AccountView
from .views.inExDetailsView import InExDetailsListView, InExDetailsCreateView, InExDetailsView
from .views.journalDetailsView import JournalDetailsCreateView, JournalDetailsListView, \
    JournalDetailsView
from .views.journalHeaderView import JournalHeaderListView, \
    JournalHeaderCreateView, JournalHeaderView
from .views.partyView import PartyListView, PartyCreateView, PartyDetailView
from .views.subscriberUsers import SubscriberUserListView, SubscriberUserCreateView, SubscriberUserDetailView
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
    path('subscriberUsers/', SubscriberUserListView.as_view()),
    path('subscriberUsers/create/', SubscriberUserCreateView.as_view()),
    path('subscriberUsers/<int:pk>/', SubscriberUserDetailView.as_view()),
    path('accounts/', AccountListView.as_view()),
    path('accounts/create/', AccountCreateView.as_view()),
    path('accounts/<int:pk>/', AccountView.as_view()),
    path('accountDetails/', AccountDetailListView.as_view()),
    path('accountDetails/create/', AccountDetailCreateView.as_view()),
    path('accountDetails/<int:pk>/', AccountDetailView.as_view()),
    path('journalHeaders/', JournalHeaderListView.as_view()),
    path('journalHeaders/create/', JournalHeaderCreateView.as_view()),
    path('journalHeaders/<int:pk>/', JournalHeaderView.as_view()),
    path('journals/', JournalDetailsListView.as_view()),
    path('journals/create/', JournalDetailsCreateView.as_view()),
    path('journals/<int:pk>/', JournalDetailsView.as_view()),
    path('parties/', PartyListView.as_view()),
    path('parties/create/', PartyCreateView.as_view()),
    path('parties/<int:pk>/', PartyDetailView.as_view()),
    path('inExDetails/', InExDetailsListView.as_view()),
    path('inExDetails/create/', InExDetailsCreateView.as_view()),
    path('inExDetails/<int:pk>/', InExDetailsView.as_view()),
    path('transactions/', TransactionsListView.as_view()),
    path('transactions/create/', TransactionsCreateView.as_view()),
    path('transactions/<int:pk>/', TransactionsDetailView.as_view()),


]