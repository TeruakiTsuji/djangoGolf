import datetime

def wdate(ymd):
	wymd = ymd[0:4] + '年' + ymd[4:6] + '月' + ymd[6:8] + '日'
	return (wymd)

def wdatey(ymd):
	y = ["月","火","水","木","金","土","日"]
	w = datetime.datetime.strptime(ymd, '%Y%m%d')
	i = w.weekday()
	ret = wdate(ymd) + '(' + y[i] + ')'
	return ret

