import time

def login():
	return 'this is a login dynamic web %s' %time.ctime()
def regist():
	return 'this is a regiest dynamic web %s' %time.ctime()
def profile():
	return 'this is profile a dynamic web %s' %time.ctime()


def application(get_file_name):
	if get_file_name == "/login.py":
		return login()
	elif get_file_name == "/regist.py":
		return regist()
	elif get_file_name == "/profile.py":
		return profile()		
	else:
		return 'no dynamic web %s' %time.ctime()