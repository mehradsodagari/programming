class Process:
    def __init__(self,pid,arrival_time,CPU_burst_time):
        self.pid = pid
        self.arrival_time = arrival_time 
        self.CPU_burst_time = CPU_burst_time 
    def __str__(self):
        return f"pid: {self.pid}, arrival_time: {self.arrival_time}, CPU_burst_time: {self.CPU_burst_time}"