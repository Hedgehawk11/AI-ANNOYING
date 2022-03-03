import pygame as game
import sys as s
import random as r
game.init()
print('\n' * 1000)
print('awncer these questions with Y OR N\n')


rick = input('do you like "never gonna give you up"')
roll = input('do you like rolling')
spam = input('do you like spam (email)')
montyspam = input('do you like monty python\'s skit "spam"')
games = input('do you like games')
sckool = input('do you think ur smarter than a group harvard \n undergrads? (intelligence test)')
e = input('are you prone to sesures')



print('\n' * 1000)
print('calculating how to annoy you')
game.time.wait(1000)
for i in range (10):
  print('\ ')
  game.time.wait(100)
  print('\n' * 1000)
  print('| ')
  game.time.wait(100)
  print('\n' * 1000)
  print('/ ')
  game.time.wait(100)
  print('\n' * 1000)
  print('- ')
  game.time.wait(100)
  print('\n' * 1000)
  print('| ')
  game.time.wait(100)
  print('\n' * 1000)
print('annoyance found')


#moved to new file

if rick == 'y':
  rickroll = False
else:
  rickroll = True
if spam == 'n' and montyspam == 'n':
  spamwmonty = True
else:
  spamwmonty = False
if e == 'y':
  induseshezuere = False
else:
  induseshezuere = True
if sckool == 'y':
  dum = True
else:
  dum = False






if rickroll:
  for i in range(20):
    
    print('never gonna give u up')
    game.time.wait(10)
    print('never gonna let u down')
    game.time.wait(10)
    print('never gonna run around')
    game.time.wait(10)
    print('and dessert you')
    game.time.wait(1000)


if spamwmonty:
  for i in range (10):
    print('spam')
    game.time.wait(10)
    print('spam')
    game.time.wait(10)
    print('spam')
    game.time.wait(10)
    print('spam')
    game.time.wait(10)
    print('spam')
    game.time.wait(10)
    print('spam')
    game.time.wait(10)
    print('spam')
    game.time.wait(10)
    print('spamety')
    game.time.wait(10)
    print('spam')
    game.time.wait(10)



if induseshezuere:
  w = game.display.set_mode([400,300])
  for i in range(2000):
    game.display.flip()
    w.fill((r.randint(0,255),r.randint(0,255),r.randint(0,255)))



















