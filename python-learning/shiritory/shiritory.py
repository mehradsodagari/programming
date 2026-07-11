class Shiritory:
    def __init__(self,game_over=False):
        self.words=[]
        self.game_over=game_over
    def restart(self):
        self.game_over=False
        self.words=[]
        return 'game restarted' 
    def play(self,word): 
        if len(self.words)==0:
            self.words.append(word)
            return self.words
        if self.words.count(word)==0 and self.words[-1][-1]==word[0]:
            self.words.append(word)
            return self.words
        else:
            self.game_over=True
            return 'game over' 
my_shiritory=Shiritory() 
def main():
    count=1
    while True:
        word=input(f"please enter the word {count} : ")
        if my_shiritory.play(word)=='game over':
            print('game over')
            break
        else:
            print((my_shiritory.words))
        count+=1
    answer=input('if you want play again?(y/n) ')
    while answer.lower() not in ['y','n']:
        print('please answer carefully.')
        answer=input('if you want play again?(y/n) ')
    if answer.lower()=='y':
        my_shiritory.restart()
        return main() 
    else:
        my_shiritory.restart()
        print('thanks for playing')
        return 
if __name__=='__main__':
    main()