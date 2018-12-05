from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


@method_decorator(login_required(login_url='login/'), name='dispatch')
class IndexView(TemplateView):
    template_name = "home/index.html"

    #@login_required(login_url='/registration/login/')
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
