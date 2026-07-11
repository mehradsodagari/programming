import json
class ToDoList:
    def __init__(self):
        name=input("what's your name? ")
        day=input("which day of the week do you want to do this? ")
        task=input("what do you want to do that day? ")
        title=input("write a title for it : ")
        self.name=name
        self.day=day 
        self.task=task
        self.title=title
        self.file_address="E:/simple project/to do list/save_people's_tasks.json"
    def add(self):
        try:
            try:
                with open(self.file_address,'r') as f:
                    people_task=json.load(f)
            except Exception as e:
                return f'error : {e}'
            if self.name not in people_task:
                people_task[self.name] = {}
            if self.day not in people_task[self.name]:
                people_task[self.name][self.day] = {}
            people_task[self.name][self.day][self.title] = self.task
            with open(self.file_address,'w',newline='') as f:
                json.dump(people_task,f,indent=4)
            return people_task
        except Exception as e:
            return f'error : {e}'
    def remove_people(self):
        try:
            with open(self.file_address,'r') as f:
                people_task=json.load(f) 
                if self.name in people_task:
                    removed_item=people_task.pop(self.name)
                else:
                    return 'this person no have list'
            with open(self.file_address,'w',newline='') as f:
                json.dump(people_task,f,indent=4) 
            return removed_item 
        except Exception as e:
            return f'error : {e}'
    def remove_task(self):
        try:
            with open(self.file_address,'r') as f:
                people_task=json.load(f) 
                if self.title in people_task[self.name][self.day]:
                    removed_item=people_task[self.name][self.day].pop(self.title)
                else:
                    return 'this task no have list'
            with open(self.file_address,'w',newline='') as f:
                json.dump(people_task,f,indent=4) 
            return removed_item 
        except Exception as e:
            return f'error : {e}'
    def show_people_tasks(self):
        try:
            with open(self.file_address,'r') as f:
                people_task=json.load(f) 
            if self.name not in people_task:
                print('you have not added your to-do list to your task list.')
                answer=input("Would you like to do this?(y/n) ")
                while answer.lower() not in ['y','n']:
                    print('please answer carefully')
                    answer=input("Would you like to do this?(y/n) ")
                if answer.lower()=='y':
                    return self.add(self)
            else:
                return people_task[self.name]
        except Exception as e:
            return f'error : {e}'
def main():
    person=ToDoList()
    while True:
        what_method=input('what do you want to do?(add/remove_people/remove_task/show_people_tasks)')
        while what_method not in ['add','remove_people','remove_task','show_people_tasks']:
            print('please answer carefully.')
            what_method=input('what do you want to do?(add/remove_people/remove_task/show_people_tasks) ')
        if what_method=='add':
            result=person.add()
        elif what_method=='remove_people':
            result=person.remove_people()
        elif what_method=='remove_task':
            result=person.remove_task()
        else:
            result=person.show_people_tasks()
        print(result)
        answer=input('do you want to do something else?(y/n) ')
        while answer not in ['y','n']:
            print('please answer carefully.')
            answer=input('do you want to do something else?(y/n) ') 
        if answer=='y':
            return main() 
        else:
            print('bye.have a good time')
            break
if __name__=='__main__':
    main()
