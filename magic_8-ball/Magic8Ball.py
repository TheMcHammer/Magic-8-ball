import random
class Fortune:
    #global fates
    fates = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes - definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful'
]

    def get_input(self, text):
        return input(text)

    def shake_8ball(self):
        shake = Fortune.get_input(self, "Shake Magic 8 ball? Y/N (press quit to stop): ")
        while shake:
            if shake == 'y':
                print('Asking fate')
                print('...')
                answer = random.choice(fates)
                print(answer)
                input('Ask a question to get an answer: ')
                Fortune.shake_8ball(self)
                return 'Yes Entered'

            elif shake == 'n':
                print('May the force be with you \n')
                break
                return 'No Entered'
            else:
                print('Invalid input')
                print()


    def give_fate(self):
        global fates
        fates = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes - definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful'
]
        input('Ask a question to get an answer: ')
        ##not tested##

        Fortune.shake_8ball(self)

            #return answer
        ####

fate = Fortune()

fate.give_fate()




'It is certain', 'It is decidedly so', 'Without a doubt', 'Yes - definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful'

