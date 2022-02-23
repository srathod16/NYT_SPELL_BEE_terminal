import os
#os.chdir('G:/My Drive/EverythingElseBackup/Python_fun_projects/NYT_SB/')
#os.chdir('/Volumes/GoogleDrive/My Drive/EverythingElseBackup/Python_fun_projects/NYT_SB/')
import numpy as np
import pandas as pd
import string
from itertools import product
from string import ascii_lowercase
import cmd
import urllib.request
import random
import collections
pl = open('sowpods.txt', 'r').read().split("\n")
npl = pl

cli = cmd.Cmd()
mode = input('Select Mode: own or random == ')


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

if mode == 'own':
  specific = input('Central Letter = ').lower()
  group = input('All letters inc central = ').lower()

if mode == 'random':
  vs = ''.join(random.sample(VOWELS, k=2))
  cs = ''.join(random.sample(CONSONANTS, k=5))
  group = cs+vs
  specific = random.choice(group)
  print('Central word = ' + specific)
  print('Todays letters are: ' + "-".join(list(group)))


group_without = "".join(sorted(group.replace(specific, ""), key = lambda x: random.random() ))

sbpl = [word for word in npl if len(word) >= 4]
fpl = [word for word in sbpl if all(letter in word for letter in specific)]
curated = [w for w in fpl if all(i in list(group) for i in w)]


scorer = []
savedwords = []

while True:
  input_word = input('Todays letters are: ' + "-".join(sorted(group, key = lambda x: random.random() ))  + ' Fixed letter = ' + specific + '\nEnter word = ').lower()
  if input_word in curated:
        if input_word in savedwords:
          print('Already guessed!\n')          
          print('           ' + group_without[0] +  '           \n' + '     ' + group_without[1] + '          ' + group_without[2] + '\n' + '           ' + specific +  '           ' +'\n'+ '     ' + group_without[3] + '          ' + group_without[4]+ '\n           ' + group_without[5] +  '           ')
          print('\n')
          continue
        if len(input_word) ==4:
          scorer.append(len(input_word))
          savedwords.append(input_word)
          print('Your score = ' + str(sum(scorer)) + '\n\n')
          print('Words guessed = ' + str(len(scorer)) + '/' + str(len(curated)) + '\n\n')
          #print('Your guessed words = \n' + '\n'.join(str(p) for p in savedwords))
          cli.columnize(sorted(savedwords), displaywidth=80)
          print('\n')
          print('           ' + group_without[0] +  '           \n' + '     ' + group_without[1] + '          ' + group_without[2] + '\n' + '           ' + specific +  '           ' +'\n'+ '     ' + group_without[3] + '          ' + group_without[4]+ '\n           ' + group_without[5] +  '           ')
          print('\n')      
        if len(input_word) > 4:
          scorer.append(len(input_word))
          savedwords.append(input_word)
          print('Your score = ' + str(sum(scorer)) + '\n\n')
          print('Words guessed = ' + str(len(scorer)) + '/' + str(len(curated)) + '\n\n')
          #print('Your guessed words = \n' + '\n'.join(str(p) for p in savedwords))
          cli.columnize(sorted(savedwords), displaywidth=80)
          print('\n')
          print('           ' + group_without[0] +  '           \n' + '     ' + group_without[1] + '          ' + group_without[2] + '\n' + '           ' + specific +  '           ' +'\n'+ '     ' + group_without[3] + '          ' + group_without[4]+ '\n           ' + group_without[5] +  '           ')
          print('\n')
  if input_word not in curated:
    print('Invalid Word\n\n')
    group_without = "".join(sorted(group.replace(specific, ""), key = lambda x: random.random() ))
    print('           ' + group_without[0] +  '           \n' + '     ' + group_without[1] + '          ' + group_without[2] + '\n' + '           ' + specific +  '           ' +'\n'+ '     ' + group_without[3] + '          ' + group_without[4]+ '\n           ' + group_without[5] +  '           ')
  
  if len(scorer) ==10:
    print('Congratulations, you guessed 10 words + ' + '\n')
    print('Words guessed = ' + str(len(scorer)) + '/' + str(len(curated)) + '\n\n')
    #print('\n'.join(str(p) for p in savedwords))
    cli.columnize(sorted(savedwords), displaywidth=80)
    print('\n')
  if input_word == 'quit':
    print('Your score = ' + str(sum(scorer)))
    print('Your guessed words = \n')
    cli.columnize(sorted(savedwords), displaywidth=80)
    print('\n')
    print('All words = \n')
    cli.columnize(curated, displaywidth=80)
    print('\n')
    qword = input('Really quit? ------- y/n: ')
    if qword == 'Y' or qword == 'y':
      break
    if qword == 'N' or qword == 'n':
      continue

  if input_word.lower() == 'score':
    print('Your score = ' + str(sum(scorer)) + '\n\n')

  if input_word.lower() == 'a hint':
    print(curated[np.random.randint(len(curated))] + '\n\n')

  if input_word.lower() == 'shuf':
    group_without = "".join(sorted(group.replace(specific, ""), key = lambda x: random.random() ))
    #print('\n\n')
    print('           ' + group_without[0] +  '           \n' + '     ' + group_without[1] + '          ' + group_without[2] + '\n' + '           ' + specific +  '           ' +'\n'+ '     ' + group_without[3] + '          ' + group_without[4]+ '\n           ' + group_without[5] +  '           ')
  


