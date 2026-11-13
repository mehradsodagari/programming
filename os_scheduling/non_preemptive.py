from process import Process
class NONPreemptive:
    def __init__(self):
        pass
    def FCFS(self,processes,cs):
        if not processes:
            return []
        sorted_processes = sorted(processes,key=lambda p: p.arrival_time)
        schedule = []
        schedule.append({"pid":"half_context_switch",
                        "start_time":sorted_processes[0].arrival_time,
                        "end_time":sorted_processes[0].arrival_time+(cs/2)})
        elapsed_time = schedule[-1]["end_time"]
        for p in range(len(sorted_processes)):
            if sorted_processes[p].arrival_time>elapsed_time:
                schedule.append({"pid":"IDLE",
                                "start_time":elapsed_time,
                                "end_time":sorted_processes[p].arrival_time}) 
                elapsed_time=schedule[-1]["end_time"]
                if p!=0:
                    schedule.append({"pid":"context_switch",
                                    "start_time":schedule[-1]["end_time"],
                                    "end_time":schedule[-1]["end_time"]+cs})
                    elapsed_time=schedule[-1]["end_time"]
                schedule.append({"pid":f"pid{sorted_processes[p].pid}",
                                "start_time":elapsed_time,
                                "end_time":elapsed_time+sorted_processes[p].CPU_burst_time}) 
                elapsed_time=schedule[-1]["end_time"]
            else:
                if p!=0:
                    schedule.append({"pid":"context_switch",
                                    "start_time":schedule[-1]["end_time"],
                                    "end_time":schedule[-1]["end_time"]+cs})
                    elapsed_time=schedule[-1]["end_time"]
                schedule.append({"pid":f"pid{sorted_processes[p].pid}",
                                "start_time":schedule[-1]["end_time"],
                                "end_time":schedule[-1]["end_time"]+sorted_processes[p].CPU_burst_time})
                elapsed_time=schedule[-1]["end_time"]
            if p==len(sorted_processes)-1:
                schedule.append({"pid":"half_context_switch",
                                "start_time":schedule[-1]["end_time"],
                                "end_time":schedule[-1]["end_time"]+(cs/2)})
            elapsed_time=schedule[-1]["end_time"]
        return schedule
    def SPN(self,processes,cs):
        if not processes:
            return []
        sorted_processes = sorted(processes,key=lambda p: (p.arrival_time,p.CPU_burst_time)) 
        length = len(sorted_processes)
        schedule = []
        queue = []
        schedule.append({"pid":"half_context_switch",
                         "start_time":sorted_processes[0].arrival_time,
                         "end_time":sorted_processes[0].arrival_time+(cs/2)})
        elapsed_time = schedule[-1]["end_time"]
        p=sorted_processes[0]
        sorted_processes.remove(p)
        for n in range(length):
            if p.arrival_time>elapsed_time:
                schedule.append({"pid":"IDLE",
                                "start_time":elapsed_time,
                                "end_time":p.arrival_time}) 
                elapsed_time=schedule[-1]["end_time"]
                if n!=0:
                    schedule.append({"pid":"context_switch",
                                    "start_time":schedule[-1]["end_time"],
                                    "end_time":schedule[-1]["end_time"]+cs})
                    elapsed_time=schedule[-1]["end_time"]
                schedule.append({"pid":f"pid{p.pid}",
                                "start_time":elapsed_time,
                                "end_time":elapsed_time+p.CPU_burst_time}) 
                elapsed_time=schedule[-1]["end_time"]
            else:
                if n!=0:
                    schedule.append({"pid":"context_switch",
                                    "start_time":schedule[-1]["end_time"],
                                    "end_time":schedule[-1]["end_time"]+cs})
                    elapsed_time=schedule[-1]["end_time"]
                schedule.append({"pid":f"pid{p.pid}",
                                "start_time":schedule[-1]["end_time"],
                                "end_time":schedule[-1]["end_time"]+p.CPU_burst_time})
                elapsed_time=schedule[-1]["end_time"]
            if sorted_processes:
                for process in sorted_processes:
                    if process.arrival_time<=elapsed_time:
                        queue.append(process)
                queue = sorted(queue,key=lambda p: p.CPU_burst_time)
                if queue:
                    p = queue[0]
                else:
                    p=sorted_processes[0]
            if n==length-1:
                schedule.append({"pid":"half_context_switch",
                                "start_time":schedule[-1]["end_time"],
                                "end_time":schedule[-1]["end_time"]+(cs/2)})
            elapsed_time=schedule[-1]["end_time"]
            queue.clear()
            if sorted_processes:
                sorted_processes.remove(p)
        return schedule