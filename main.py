#pip install python-telegram-bot==13.14
#python ./main.py --id 010-4442-5552 --pw Dighwjdgh3# --dep 수서 --arr 동대구 --date 20230929 --start 100000 --end 120000 --iter 3 --seat 일반실
from korail2 import *
import telegram
import time as timer
import argparse

if __name__ == "__main__":
    api_key = '5957545379:AAFAHTqrMAqMAWUsD9EkT3XvLcsu0snQgRV'
    chatId = '5517769457'
    bot = telegram.Bot(token=api_key)
    for item in bot.getUpdates():
        print(item)
    
    parser = argparse.ArgumentParser(description='SRT Reservation')
    parser.add_argument('--id', default="")
    parser.add_argument('--pw', default="")
    parser.add_argument('--dep', default="서울")
    parser.add_argument('--arr', default="동대구")
    parser.add_argument('--date', default="20230929")
    parser.add_argument('--start', default="090000")
    parser.add_argument('--end', default="140000")
    parser.add_argument('--iter', default="1000")
    parser.add_argument('--seat', default="일반실")
    args = parser.parse_args()
    print(args)

    korail = Korail(args.id, args.pw, auto_login=False)
    korail.login()
    dep = args.dep
    arr = args.arr
    date = args.date
    time = args.start
    time_limit = args.end
    iter = args.iter
    seatType = args.seat
  
    for k in range(1, int(iter)+1):
        # trains = srt.search_train(dep, arr, date, time, time_limit)
        trains = korail.search_train(dep, arr, date, time, train_type=TrainType.KTX)

        print("\r"+str(k), end="")
        
        for i in range(0, len(trains)):
            print(trains[i])
        j = 0
        for j in range(0, len(trains)):
            if seatType in str(trains[j]):
                try:
                    reservation = korail.reserve(trains[j])
                    print(reservation)
                    bot.sendMessage(chat_id=chatId, text="[KTX] " + str(reservation))
                    continue
                except:
                    continue
        timer.sleep(1)

