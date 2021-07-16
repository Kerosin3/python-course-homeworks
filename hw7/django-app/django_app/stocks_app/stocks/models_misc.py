import time,datetime
import random
import string

def get_cur_data():
    # 14/07/2021:15:23:09.930 format
    time.sleep(0.05)
    now = datetime.datetime.now()
    ret = (now.strftime("%d/%m/%Y:%H:%M:%S.%f")[:-3])
    return ret

def gen_ticker():
    return ''.join(random.sample(string.ascii_uppercase, 4))

def get_rand_data():
    return round(random.uniform(0, 200), 3)
