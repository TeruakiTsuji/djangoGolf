from django.shortcuts import render
from django.views.generic import TemplateView

import datetime
from index import LocalDate
#from index import Sqlite
from index import Database

# Create your views here.
class NextTemplateView(TemplateView):

    template_name = 'next.html'

    def get(self, request, *args, **kwargs):

        results = [];
        dt_now = datetime.datetime.now()
        today = dt_now.strftime('%Y%m%d')
        result = Database.execute('select * from next where open_dt >= \'' + today + '\' order by open_dt')

        for row in result:
        	wdate = LocalDate.wdatey(row[0])
        	row = { 'open_dt' : wdate, 'place' : row[1] }
        	results.append(row)

        context = {
            'app' : 'Next',
            'results' : results
        }
        return render(self.request, self.template_name, context)

