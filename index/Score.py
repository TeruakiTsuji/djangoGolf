import datetime

def num2disp_num(num):
	ret = ''
	if num == 1:
		ret = '優勝'
	elif num == 2:
		ret = '準優勝'
	else:
		ret = '第' + str(num) + '位'

	return ret

