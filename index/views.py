from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        #context = super(TemplateView, self).get_context_data(**kwargs)
        context = {
            'app': 'index'
        }
        return render(self.request, self.template_name, context)
