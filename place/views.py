from django.shortcuts import render
from django.views.generic import TemplateView

import datetime
from index import LocalDate
from index import Sqlite
from index import Users

# Create your views here.
class PlaceTemplateView(TemplateView):

    template_name = 'place.html'

    def get(self, request, *args, **kwargs):

        results = [];
        dt_now = datetime.datetime.now()
        result = Sqlite.execute('select * from tran_place order by date')
        users = Sqlite.execute('select * from users')

        for row in result:
        	wdate = LocalDate.wdatey(row[0])
        	victor = row[5]
        	victor_nm = Users.name_num2disp_name(users,victor)
        	bg1 = row[6]
        	bg1_nm = Users.name_num2disp_name(users,bg1)
        	bg2 = row[7]
        	bg2_nm = Users.name_num2disp_name(users,bg2)
        	bg3 = row[8]
        	bg3_nm = Users.name_num2disp_name(users,bg3)
        	if len(bg3) == 0:
        		if len(bg2) == 0:
        			bg_nm = bg1_nm
        		else:
        			bg_nm = bg1_nm + ', ' + bg2_nm
        	else:
        		bg_nm = bg1_nm + ', ' + bg2_nm + ', ' + bg3_nm

        	row = { 'date' : row[0], 'wdate' : wdate, 'place' : row[1], 'name' : row[2], 'cose1': row[3], 'cose2' : row[4],
			'victor' : victor_nm, 'bg' : bg_nm,
		}
        	results.append(row)

        context = {
            'app' : 'Place',
            'results' : results
        }
        return render(self.request, self.template_name, context)

