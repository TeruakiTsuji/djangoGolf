import datetime

def name_num2disp_name(users,name_num):
	ret = ''
	idx_name_num = 0
	idx_disp_name = 9
	for user in users:
		if user[idx_name_num] == name_num:
			ret = user[idx_disp_name]
			break

	return ret

