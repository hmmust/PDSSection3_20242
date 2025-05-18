import multiprocessing
import time

print(multiprocessing.cpu_count())
def calc_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
        time.sleep(0.5)
        print(n,sum)
    return sum
if __name__ == '__main__':
    sum_pool = multiprocessing.Pool(processes=2)
    sum1 = sum_pool.apply(calc_sum,args=(5,))
    sum2 = sum_pool.apply(calc_sum,args=(10,))
    # call funtion 
    sum_pool.close()
    sum_pool.join()
    print("Done calculation!",sum1,sum2)
    
    
