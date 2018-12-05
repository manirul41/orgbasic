from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "about/about.html"


class ShowAllMembers(TemplateView):
    template_name = "about/members.html"


class ShowMemberDetails(TemplateView):
    template_name = "about/member_details.html"
