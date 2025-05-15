import multiprocessing
import time

print(multiprocessing.cpu_count())
def print_hossams(n):
    for i in range(1,n+1):
        print(n,'Hossam '*i)
        time.sleep(0.5)
def print_miras(n):
    for i in range(1,n+1):
        print(n,'Mira '*i)
        time.sleep(0.5)
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=print_hossams,args=(3,))
    p2 = multiprocessing.Process(target=print_miras,args=(4,))
    p1.start()
    #p1.join() # sequential
    p2.start()
    p1.join()
    p2.join()
    print("Done printing!")
    
    
