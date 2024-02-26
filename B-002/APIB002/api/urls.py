from django.urls import path
from .views import CryptoCurrencyView, CryptoCurrencyHistoryView, CryptoCurrencyHistoryListView


urlpatterns=[
    path('currencies/',CryptoCurrencyView.as_view(),name='curriencies_list'),
    path('currencies/<int:ID>',CryptoCurrencyView.as_view(),name='curriencies_process'),

    path('currencies/history',CryptoCurrencyHistoryView.as_view(),name='curriencies_history_list'),
    path('currencies/history/<int:ID>',CryptoCurrencyHistoryView.as_view(),name='curriencies_history_process'),

    path('crypto/currency/histories/', CryptoCurrencyHistoryListView.as_view(), name='crypto_currency_histories')
]

