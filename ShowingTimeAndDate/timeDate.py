import os, time, platform as pt

def refresh() :
    # For Mac or Linux OS
    if pt.system() == 'Linux' or pt.system() == 'Darwin' : os.system('clear')
    else : os.system('cls') # for  Windows Operation System

while True : 
	# return array 
    time_r = time.localtime()
    
    year,month,day,hour,minute,second = time_r[0],time_r[1],time_r[2],time_r[3],time_r[4],time_r[5]

    print('''	Date:	{}-{}-{}
    	Time:	{}:{}:{}'''.format(month,day,year,hour,minute,second)) 
    time.sleep(1)
    refresh()
