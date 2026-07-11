from hospital2 import Queue 
from datetime import datetime
from colorama import Fore,Style
class Hospital(Queue):
    def __init__(self):
        super().__init__() 
        self.visited_patients=[]
    def patient(self,name,lastname,id,age,blood_type,status):
        try:
            patient_datails={'name':name,
                            'lastname':lastname,
                            'id':id,
                            'age':age,
                            'blood type':blood_type,
                            'arrival time':datetime.now(),
                            'status':status}
            if self.head is None:
                return self.enqueue(patient_datails) 
            index=0
            probe=self.head 
            while probe!=self.tail and probe.data['status']<=patient_datails['status']:
                probe=probe.next
                index+=1 
            if probe is None:
                if self.tail.data['status']<=patient_datails['status']:
                    return self.inserting_at_the_end(patient_datails)
                else:
                    index+=1 
                    return self.inserting_at_any_position(patient_datails,index)
            else:
                return self.inserting_at_any_position(patient_datails,index)
        except Exception as e:
            return f'error : {e}'
    def next_patient(self):
        try:
            if self.head is None:
                return 'there are no patient in this hospital'
            patient=self.peek()
            if patient is None:
                return 'there are no patient in this hospital'
            if isinstance(patient,dict):
                if patient['status']==1:
                    return Fore.RED + patient['name'] + Style.RESET_ALL
                if patient['status']==2:
                    return Fore.YELLOW + patient['name'] + Style.RESET_ALL
                if patient['status']==3:
                    return Fore.GREEN + patient['name'] + Style.RESET_ALL 
            return 'there are no patient in this hospital'
        except Exception as e:
            return f'error : {e}'
    def visit(self):
        try:
            if self.head is None:
                return 'there are no patient in this hospital'
            patient=self.dequeue()
            self.visited_patients.append(patient)
            if patient['status']==1:
                return Fore.RED + f'''patient information 
    name : {patient['name']}
    latname : {patient['lastname']}
    id : {patient['id']}
    age : {patient['age']}
    blood type : {patient['blood type']}
    arrival time : {patient['arrival time']}
    status : {patient['status']}''' + Style.RESET_ALL
            if patient['status']==2:
                return Fore.YELLOW + f'''patient information 
    name : {patient['name']}
    latname : {patient['lastname']}
    id : {patient['id']}
    age : {patient['age']}
    blood type : {patient['blood type']}
    arrival time : {patient['arrival time']}
    status : {patient['status']}''' + Style.RESET_ALL
            if patient['status']==3:
                return Fore.GREEN + f'''patient information 
    name : {patient['name']}
    latname : {patient['lastname']}
    id : {patient['id']}
    age : {patient['age']}
    blood type : {patient['blood type']}
    arrival time : {patient['arrival time']}
    status : {patient['status']}''' + Style.RESET_ALL
        except Exception as e:
            return f'error : {e}'
    def searching_patient(self,patient_inforamtion):
        try:
            if self.head is None:
                return 'there are no petient in this hospital'
            if patient_inforamtion.isdigit():
                probe=self.head 
                while probe!=self.tail and probe.data['id']!=patient_inforamtion:
                    probe=probe.next 
                if self.tail.data['id']==patient_inforamtion:
                    return self.tail.data 
                if probe is None:
                    return f'there is no patient with this id ({patient_inforamtion}) in this hospital.'
                return probe.data
            else:
                name,lastname=patient_inforamtion.split()
                probe=self.head 
                while probe!=self.tail and probe.data['name']!=name and probe.data['lastname']!=lastname:
                    probe=probe.next 
                if self.tail.data['name']==name and self.tail.data['lastname']==lastname:
                    return self.tail.data
                if probe is None:
                    return f'there is no patient with this name ({name} {lastname}) in this hospital.'
                return probe.data
        except Exception as e:
            return f'error : {e}'
    def find_patient(self,patient_inforamtion):
        try:
            if self.head is None:
                return 'there are no petient in this hospital'
            if patient_inforamtion.isdigit():
                probe=self.head 
                while probe!=self.tail and probe.data['id']!=patient_inforamtion:
                    probe=probe.next 
                if self.tail.data['id']==patient_inforamtion:
                    return self.tail 
                if probe is None:
                    return f'there is no patient with this id ({patient_inforamtion}) in this hospital.'
                return probe
            else:
                name,lastname=patient_inforamtion.split()
                probe=self.head 
                while probe!=self.tail and probe.data['name']!=name and probe.data['lastname']!=lastname:
                    probe=probe.next 
                if self.tail.data['name']==name and self.tail.data['lastname']==lastname:
                    return self.tail
                if probe is None:
                    return f'there is no patient with this name ({name} {lastname}) in this hospital.'
                return probe
        except Exception as e:
            return f'error : {e}'
    def change_status(self,patient_information,new_status):
        try:
            node=self.find_patient(patient_information)
            if not hasattr(node,'data'):
                return 'there is no patient with this details' 
            data=node.data 
            self.removing_at_any_position(node)
            data['status']=new_status 
            self.patient(data['name'],
                data['lastname'],
                data['id'],
                data['age'],
                data['blood type'],
                data['status'],
            )
        except Exception as e:
            return f'error : {e}' 
    def remove_patient(self,patient_information):
        try:
            if self.find_patient(patient_information)=='there are no patient on the list':
                    return 'there is no patient with this details'
            patient=self.find_patient(patient_information)
            if patient['status']==0:
                print('the patient was discharged')
            if patient['status']==-1:
                print('the patient died')
            return self.removing_at_any_position(patient)
        except Exception as e:
            return f'error : {e}'
    def count_by_status(self,status):
        try:
            if self.head is None:
                return 'there are no patient in this hospital' 
            probe=self.head  
            count=0
            while probe!=self.tail:
                if probe.data['status']==status:
                    count+=1
                    probe=probe.next 
                if self.tail.data['status']==status:
                    count+=1 
            if count>10:
                return Fore.RED + f'{count}'
            return count
        except Exception as e:
            return f'error : {e}'
    def show_by_status(self,status):
        try:
            if self.head is None:
                return 'there are no patient in this hospital' 
            probe=self.head  
            while probe!=self.tail:
                if probe.data['status']==status:
                    print(Fore.RED + probe.data)
                    probe=probe.next 
                if self.tail.data['status']==status:
                    print(Fore.RED + self.tail.data)
        except Exception as e:
            return f'error : {e}'
    def check_exist_status(self):
        try:
            if self.head is None:
                return 'there are no patient in this hospital' 
            if self.count_by_status(1)>0:
                return True 
            return False
        except Exception as e:
            return f'error : {e}'
    def get_statistics(self):
        try:
            patient=self.peek() 
            if patient['status']==1:
                color=Fore.RED
            if patient['status']==2:
                color=Fore.YELLOW
            if patient['status']==3:
                color=Fore.GREEN
            return f''' {Fore.YELLOW + 'hospital statistics'}hospital statistics
{Fore.RED + f'total number of patient : {self._CircularLinkedList__size}'+ Style.RESET_ALL}
{Fore.RED + f'People with the status 1 : {self.count_by_status(1)}'+ Style.RESET_ALL}
{Fore.YELLOW + f'People with the status 2 : {self.count_by_status(2)}'+ Style.RESET_ALL}
{Fore.GREEN + f'People with the status 3 : {self.count_by_status(3)}'+ Style.RESET_ALL}
{color + f'next patient : {self.next_patient()}'+ Style.RESET_ALL}
'''
        except Exception as e:
            return f'error : {e}'
    def has_emergency(self):
        try:
            if self.count_by_status(1)>0:
                return Fore.RED + Style.BRIGHT + f'We have {self.count_by_status(1)} to emergency patients'
            return "we don't have emergency patient"
        except Exception as e:
            return f'error : {e}'
    def check_long_waiting(self):
        try:
            if self.head is None:
                return 'there are no patient in this hospital'
            probe=self.head 
            while probe!=self.tail:
                if (datetime.now()-probe.data['arrival time']).total_seconds/60>30:
                    print(Fore.RED + Style.BRIGHT + f'the patient {probe.data['name']} {probe.data['lastname']} has been waiting for more than 30 minutes.')
            if (datetime.now()-self.tail.data['arrival time']).total_seconds/60>30:
                print(Fore.RED + Style.BRIGHT + f'the patient {self.tail.data['name']} {self.tail.data['lastname']} has been waiting for more than 30 minutes.')
        except Exception as e:
            return f'error : {e}'

