from django.urls import path, include

from Ahercode.views.crmView import CRMCreateView, CRMListView, CRMView
from WepAPI import settings
from django.conf.urls.static import static

from .views.accountDetailsView import AccountDetailView, AccountDetailListView, AccountDetailCreateView
from .views.accountView import AccountListView, AccountCreateView, AccountView
from .views.assetsView import AssetsListView, AssetsCreateView, AssetsView
from .views.calendarEventsView import CalendarEventListView, CalendarEventCreateView, CalendarEventView
from .views.inExDetailsView import InExDetailsListView, InExDetailsCreateView, InExDetailsView
from .views.journalDetailsView import JournalDetailsCreateView, JournalDetailsListView, \
    JournalDetailsView
from .views.journalHeaderView import JournalHeaderListView, \
    JournalHeaderCreateView, JournalHeaderView
from .views.partyView import PartyListView, PartyCreateView, PartyDetailView
from .views.subscriberUsersView import SubscriberUserListView, SubscriberUserCreateView, SubscriberUserDetailView
from .views.transactionsView import TransactionsListView, TransactionsDetailView, TransactionsCreateView
from .views.userView import UserCreateView, UserListView, UserDetailView
from .views.authView import LoginView, ChangePasswordView, ResetPasswordView
from .views.subscriberView import SubscriberListView, SubscriberCreateView, SubscriberDetailView, SubscriberApprovalView, SubscriberTransactionDetailsView, SubscriberTransactionSummaryView


urlpatterns = [
    
    path('users/', UserListView.as_view()),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('auth/reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('users/create/', UserCreateView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('subscribers/', SubscriberListView.as_view()),
    path('subscribers/create/', SubscriberCreateView.as_view()),
    path('subscribers/approval/<int:subscriber_id>/', SubscriberApprovalView.as_view(), name='subscriber-approval'),
    path('subscribers/<int:pk>/', SubscriberDetailView.as_view()),
    path('subscriberUsers/', SubscriberUserListView.as_view()),
    path('subscriberUsers/create/', SubscriberUserCreateView.as_view()),
    path('subscriberUsers/<int:pk>/', SubscriberUserDetailView.as_view()),
    path('subscribers/transaction-summary/', SubscriberTransactionSummaryView.as_view(), name='subscriber-transaction-summary'),
    path('subscribers/transaction-details/', SubscriberTransactionDetailsView.as_view(), name='transaction-details'),
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
    path('calendarEvents/', CalendarEventListView.as_view()),
    path('calendarEvents/create/', CalendarEventCreateView.as_view()),
    path('calendarEvents/<int:pk>/', CalendarEventView.as_view()),
    path('crm/', CRMListView.as_view()),
    path('crm/create/', CRMCreateView.as_view()),
    path('crm/<int:pk>/', CRMView.as_view()),
    path('assets/', AssetsListView.as_view()),
    path('assets/create/', AssetsCreateView.as_view()),
    path('assets/<int:pk>/', AssetsView.as_view()),
] 