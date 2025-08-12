#multithreading

from threading import Thread

def square_numbers():
    result=0
    for i in range(1000):
        result += i * i
    print(result)
      
threads = []
num_threads = 1000


for i in range(num_threads):
    thread = Thread(target=square_numbers)
    threads.append(thread)


for thread in threads:
    thread.start()


for thread in threads:
    thread.join()