import time
lights = [
  ('green' , 2),
   ('yellow', 0.5),
    ('red', .2)
]
i = 0
while True:
   c,s = lights[i]
   print (c)
   time.sleep(s)
   if i  == len(lights)-1:
       i = 0
   else:
       i +=1
       import time
       from intertools import cycle
       lights = [
               ('green',2),
               ('yellow',0.5),
               ('red,'2)
               ]
       colors = cycle(lights)
       while True:
               C,S = next(colors)
               print(c)
               time.sleep(s)
print("Bhrama")
print("Chinna")

