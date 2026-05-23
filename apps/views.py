from django.views.generic import TemplateView



class HomeViewL(TemplateView):
    template_name = 'home.html'



class AdminPageView(TemplateView):
 template_name = 'admin_page.html'




class AdminPageMarketView(TemplateView):
    template_name = 'admin_page_market.html'




class AdminPageRequestsView(TemplateView):
    template_name = 'admin_page_requests.html'



class AdminPageUrlsView(TemplateView):
    template_name = 'admin_page_urls.html'



class AdminPageStatsView(TemplateView):
    template_name = 'admin_page_stats.html'


class AdminPageCompetitionView(TemplateView):
    template_name = 'adminPage_competition.html'


class AdminPageWithdrawView(TemplateView):
    template_name = 'adminPage_withdraw.html'



class ProfileReferralView(TemplateView):
    template_name = 'adminPage_referral.html'



class ProfileSetttingsView(TemplateView):
    template_name = 'admin_seting.html'