#multiprocessing

from multiprocessing import Process
import os
def square_numbers():
    result=0
    for i in range(10):
        result += i * i
    print(result)
      
processes = []
num_processes = 10
print(os.cpu_count())
if __name__ == "__main__":
    for i in range(num_processes):
        process = Process(target=square_numbers)
        processes.append(process)


    for process in processes:
        process.start()


    for process in processes:
        process.join()