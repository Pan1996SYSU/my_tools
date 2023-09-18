import threading
import time

def worker(event):
    print("Worker started")
    time.sleep(2)  # 模拟耗时操作
    print("Worker finished")
    event.set()  # 设置事件，表示线程执行完毕

# 创建一个Event对象
event = threading.Event()

# 创建多个线程
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(event,))
    threads.append(t)
    t.start()

# 等待所有线程执行完毕
for t in threads:
    t.join()

# 判断所有线程是否全部执行完毕
if event.is_set():
    print("All threads finished")
else:
    print("Some threads are still running")
