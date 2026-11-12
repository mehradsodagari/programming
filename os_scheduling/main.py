import os
from process import Process 
from non_preemptive import NONPreemptive 
def main():
    np = NONPreemptive()
    try:
        how_many=int(input("How many processes do you have: "))
    except ValueError:
        os.system("cls")
        how_many=int(input("How many processes do you have: "))
    counter=1
    os.system("cls")
    processes = [] 
    while counter<=how_many:
        try:
            arrival_t = float(input(f"Enter the arrival time of process {counter}: "))
        except ValueError:
            os.system("cls")
            arrival_t = float(input(f"Enter the arrival time of process {counter}: "))
        try:
            burst_t = float(input(f"Enter the CPU burst time of process {counter}: "))
        except ValueError:
            os.system("cls")
            burst_t = float(input(f"Enter the CPU burst time of process {counter}: "))
        process = Process(counter,arrival_t,burst_t)
        processes.append(process)   
        os.system("cls")
        counter+=1
    try:
        context_switch = float(input("Enter the context switch: "))
    except ValueError:
        os.system("cls")
        context_switch = float(input("Enter the context switch: "))
    results = np.FCFS(processes,context_switch)
    for result in results:
        print(result)
if __name__=="__main__":
    main()
