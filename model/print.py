# coding=utf-8
from time import sleep, ctime
import threading
class prin():
    def player(name):
        for i in range(2):
            with open(r'E:\Code\PyCharmCode\xuanKe\file\p.txt', 'a') as f:
                f.write(str(name.get("cname"))+'\n')
        sleep(1)
    def run(self,list):
        threads = []
        files = range(len(list))
        # 创建线程
        for i in files:
            t = threading.Thread(target=prin.player, args=(list[i],))
            threads.append(t)
        # 启动线程
        for i in files:
            threads[i].start()
if __name__ == '__main__':
    list=[1,2]
    p = prin()
    p.run(list)