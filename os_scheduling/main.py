import os
from process import Process 
from non_preemptive import NONPreemptive 
from preemptive import Preemptive
def main():
    np = NONPreemptive()
    p = Preemptive()
    try:
        which_algorithms = int(input("Which of the following algorithms would ypu like to run:\n1_ FCFS\n2_ SPN\n3_ HRRN\n4_ RR\n5_ SRTF\n6_ MLFQ \n"))
        os.system("cls")
        while not 1<=which_algorithms<=6:
            which_algorithms = int(input("Which of the following algorithms would ypu like to run: \n1_ FCFS\n2_SPN\n3_HRRn4_RR\n5_SRTF\n6_MLFQ"))
            os.system("cls")
    except ValueError:
        which_algorithms = int(input("Which of the following algorithms would ypu like to run: \n1_ FCFS\n2_SPN\n3_HRRn4_RR\n5_SRTF\n6_MLFQ"))
        while not 1<=which_algorithms<=6:
            which_algorithms = int(input("Which of the following algorithms would ypu like to run: \n1_ FCFS\n2_SPN\n3_HRRn4_RR\n5_SRTF\n6_MLFQ"))
            os.system("cls")
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
        os.system("cls")
    except ValueError:
        os.system("cls")
        context_switch = float(input("Enter the context switch: "))
    if 4<=which_algorithms<=6:
        try:
            quantun_time = float(input("Enter the quantum time : "))
            os.system("cls")
        except ValueError:
            quantun_time = float(input("Enter the quantum time : "))
            os.system("cls")
    if which_algorithms==1:
        results = np.FCFS(processes,context_switch,)
    elif which_algorithms==2:
        results = np.SPN(processes,context_switch,)
    elif which_algorithms==3:
        results = np.HRRN(processes,context_switch,)
    elif which_algorithms==4:
        results = p.RR(processes,context_switch,quantun_time)
    elif which_algorithms==5:
        results = p.SRTF(processes,context_switch,quantun_time)
    else:
        results = p.MLFQ(processes,context_switch,quantun_time)
    for result in results:
        print(result)
if __name__=="__main__":
    main()
