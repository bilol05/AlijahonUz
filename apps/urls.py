"""
URL configuration for alijahonuz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from apps.views import HomeViewL, AdminPageView, AdminPageMarketView, AdminPageRequestsView, AdminPageUrlsView, \
    AdminPageStatsView, AdminPageCompetitionView, AdminPageWithdrawView, ProfileReferralView, ProfileSetttingsView

urlpatterns = [
    path("", HomeViewL.as_view()),
    path("admin_page/", AdminPageView.as_view()),
    path("admin_page/market", AdminPageMarketView.as_view()),
    path("admin_page/requests", AdminPageRequestsView.as_view()),
    path("admin_page/urls", AdminPageUrlsView.as_view()),
    path("admin_page/stats",AdminPageStatsView.as_view()),
    path("admin_page/competition",AdminPageCompetitionView.as_view()),
    path("admin_page/withdraw",AdminPageWithdrawView.as_view()),
    path("profile/referral",ProfileReferralView.as_view()),
    path("profile/settings",ProfileSetttingsView.as_view()),
]
