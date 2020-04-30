from bs4 import BeautifulSoup as bs
import requests as rq
from datetime import timedelta,datetime as dt

response = rq.get("https://www.hurriyet.com.tr/ramazan/ankara-imsakiye/").content 


sp = bs(response,"html.parser")
 
datas = sp.find_all("tr")
d = []
for i in datas:
    # print(i.text.strip()) 
    d.append(i.text.strip())    
# print("========================================")

ramadan_dates = []
iftar_time = []
for i in range(len(d)):
    # print(d[i].split()[1])
    ramadan_dates.append(d[i].split()[1])
for i in range(len(d)):
    # print(d[i].split()[6])
    iftar_time.append(d[i].split()[6])
# print(len(ramadan_dates),len(iftar_time))
new = zip(ramadan_dates,iftar_time)




def time_now(): 
    now = dt.now()
    
    if now.day < 10 : day = '0'+str(now.day)
    else : day = str(now.day)
    if now.month < 10 : month =  '0'+str(now.month)
    else : month = str(now.month)
    year = str(now.year )
    today = day+'.'+month+'.'+year
    return today

times = {}

for i,j in new :

    times[i] = j

def imsakiye() :
    year = dt.now().year
    
    print(
        """
                ==========================
                    {} Imsakiye 
                Today : {}
                ==========================
        """.format(year,time_now()))
    for i,j in times.items():
        print('\t\t',i,' ',j)

def calc_time () :
    today_iftar = times[time_now()]
    t_i = today_iftar.split(":")
    
    old_time = dt.now()
    
    now_time = timedelta(hours=old_time.hour, minutes=old_time.minute)
    iftar_time_ = timedelta(hours=int(t_i[0]), minutes=int(t_i[1]))
    
    new_time = iftar_time_ - now_time
    print(
        '''
        ================================
            Today : {} 
            Iftar Time : {}
            Remaining Time : {}
        ================================
        '''.format(time_now(),today_iftar,new_time)
    )

def main() : 
    print(
        '''
        =====================================
                        Welcome 

                For Imsakiye  press 1

                Show to Remaining 
                Time to Iftar press  2

        =====================================
        '''
    )    
    
    




if __name__ == "__main__":
    main()
    try : user_choice = int(input(": ")) 

    except ValueError:
        print('Oops! That was no valid number. Try Again...')

    if user_choice == 1 :
        imsakiye()
    elif user_choice == 2 :
        calc_time()
    else :
        print('Oops! That was no valid number. Try Again...')