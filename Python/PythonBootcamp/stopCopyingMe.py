# convo = input('hey how is it going? ')

# while convo != 'stop':
#     print(convo)
#     convo = input()
# print('ok ok')


times = input('how many times do I have to tell you? ')
times = int(times)

for time in range(times):
    print(f"time {time}: clean the room")
    if time >= 4:
        print('do you even listen to me?')
        break