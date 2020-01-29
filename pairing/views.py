from django.shortcuts import render
from django.views.generic import TemplateView

import datetime
from index import LocalDate
from index import Sqlite

# Create your views here.
class PairingTemplateView(TemplateView):

    template_name = 'pairing.html'

    def get(self, request, *args, **kwargs):

        print(request)
        parm = request.path
        parms = parm.split('/');
        arg_1 = '1' in parms
        if arg_1 == True:
        	print ('arg (1)')
        	dt_now = datetime.datetime.now()
        	from_dt = dt_now.strftime('%Y') + '0101'
        	result = Sqlite.execute('select * from pairing where open_dt >= \'' + from_dt + '\' order by open_dt')
        else:
        	print ('arg (0)')
        	print (len(parms))
        	if len(parms) == 3 and len(parms[2])>0:
        		open_dt = parms[2]
        		print ('open_dt:' + open_dt)
        		result = Sqlite.execute('select * from pairing where open_dt = \'' + open_dt + '\' order by open_dt')
        	else:
        		result = Sqlite.execute('select * from pairing order by open_dt')

        users = Sqlite.execute('select * from users')
        results = [];

        for row in result:
        	wdate = LocalDate.wdatey(row[0])
        	row = { 'open_dt' : row[0], 'wdate' : wdate, 'num' : row[1], 'start_tm' : row[2], 'cose1': row[3], 'cose2' : row[4],
			'code1' : row[5], 'code2' : row[6],'code3' : row[7],'code4' : row[8],
		}
        	results.append(row)

        context = {
            'app' : 'Pairing',
            'results' : results
        }
        return render(self.request, self.template_name, context)

