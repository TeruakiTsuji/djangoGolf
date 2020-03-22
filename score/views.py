from django.shortcuts import render
from django.views.generic import TemplateView

import datetime
from index import LocalDate
#from index import Sqlite
from index import Database
from index import Users
from index import Score

# Create your views here.
class ScoreTemplateView(TemplateView):

    template_name = 'score.html'

    def get(self, request, *args, **kwargs):

        parm = request.path
        parms = parm.split('/');
        if len(parms) == 3 and len(parms[2]) > 0:
        	open_dt = parms[2]
        	result = Database.execute('select * from tran_score where date = \'' + open_dt + '\' order by date, num')
        else:
        	result = Database.execute('select * from tran_score order by date, num')

        users = Database.execute('select * from users')
        results = [];

        for row in result:
        	wdate = LocalDate.wdatey(row[0])
        	num = row[1]
        	wnum = Score.num2disp_num(num)
        	name_num = row[2]
        	disp_name = Users.name_num2disp_name(users,name_num)
        	row = { 'date' : row[0], 'wdate' : wdate, 'num' : wnum, 'name' : disp_name, 'score1': row[3], 'score2' : row[4],
			'gross' : row[5], 'hdcp' : row[6], 'net' : row[7],
		}
        	results.append(row)

        context = {
            'app' : 'Score',
            'results' : results,
            'open_dt' : open_dt
        }
        return render(self.request, self.template_name, context)

