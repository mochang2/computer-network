from telepot import Bot
from requests import get
from apscheduler.schedulers.blocking import BlockingScheduler as scheduler
from datetime import datetime
import csv

def get_requests_and_save():
    #request and print
    now = datetime.now()
    nowDateTime=now.strftime("%Y-%m-%d-%H-%M")
    r = get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,KRW")
    data = eval(r.text)
    USD = data["USD"]
    EUR = data["EUR"]
    KRW = data["KRW"]
    print(nowDateTime, r.text)

    #write csv
    f = open("more_price.csv", "a", newline="")
    wr=csv.writer(f)
    wr.writerow([nowDateTime, USD, EUR])
    f.close()

    #receive msg from chat bot
    global bot, li
    str0 = "Bithumb-BTC-KRW: "
    if len(li) == 0: #only one element
        li.append(KRW)
        price_change = KRW
    else:
        li.append(KRW)
        price_change = li[1] - li[0]
        li.pop(0) #remove data extracted before 1 minute

    bot.sendMessage(chat_id = 1224394616, text =(str0 + str(KRW) + ", UP " + str(price_change) ))


if __name__ == "__main__":
    token = "1035176922:AAEag0yoE6IEUDp5p6ZWOfA2BmOFL7l7lcY"
    bot = Bot(token) #chat bot
    li = [] # to observe price_change

    sched = scheduler()
    sched.add_job(get_requests_and_save, "interval", seconds=60) #execute function every 60 seconds
    sched.start()
