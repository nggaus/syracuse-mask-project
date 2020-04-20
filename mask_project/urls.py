"""
@Copyright Michelle Mark 2018
@author Michelle Mark

"""
from django.urls import path

from . import views


urlpatterns = [
    path('request-donations/',
         views.RequestDonationsView.as_view(),
         name='request-donations'),
    path('request-donations-thanks/',
         views.RequestDonationsThanksView.as_view(),
         name='request-donations-thanks')
]
