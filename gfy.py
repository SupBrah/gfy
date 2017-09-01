#!/usr/bin/env python3

import random
from flask import Flask
from foaas import Fuck

app = Flask(__name__)
fuck = Fuck(secure=True)


#  class GoFuckYourself:
#      """Hey $luser, GoFuckYourself()"""
#      def init(self, *args, **kwargs):

#          self.man = ['Evan', 'Matt']
#          self.beast = ['Shardik', 'Linus']
#          self.all = man + beast
#          print(self.all)

man = ['Evan', 'Matt']
beast = ['Shardik', 'Linus']
both = man + beast


def no_doubles():
    name = random.choice(both)
    from_ = random.choice(both)
    nf_dict = {}

    while name != from_:
        nf_dict[name] = from_
        return nf_dict
    else:
        pass


while no_doubles is None:
    if no_doubles() is not None:
        print(no_doubles())
    else:
        print('was None')
        no_doubles()
else:
    print(no_doubles())


def make_italics():
    decorator = True
    gg

@app.route('/')
def hiya():
    #  pass
    #  return fuck.random(name=no_doubles()[0], from_=no_doubles()[1]).text
    return fuck.random(name='Shardik', from_='Linus').text

@app.route('/fuck')
def fuck_off():
    return 'Go Fuck Yourself.'


#  if __name__ == '__main__':
#      #  F = GoFuckYourself()
#      hiya()
