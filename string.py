print('hello world')
print('this is \n string')
print('good morning')
print('\n')
print('good night')

len('hello world')


s='hello world'
print(s)
print(s[0])
print(s[6])
print(s[3])

print(s[1:])
print(s[:4])
print(s[:-1])
print(s[-3])
print(s[::-2])
print(s[:])
print(s[::-3])

#concatenate string
s='heyy'
s=s +"\ti'm student"
print(s)

letter ='n'
print(letter*10)
string='nidhi'
print(string*5)


m='i am hungry'
print(m.upper())
print(m.lower())
print(m.split())
print(m.split('h'))


#string formating
print('this is a string {}'.format('insert'))
print('the {2} {1} {0}'.format('pizza','burger','frankie'))
print('the object {a},the object {b},the object {c}'.format(a=12,b='two',c=1.5))
print('a {p} saved is a {p} earned'.format(p='penny'))

#assign field length left&right
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))

#left, center & right allignment
print('{0:=<8} | {1:-^8} | {2:*>8}'.format('left','center','right'))
print('{0:=<8}| {0:-^8} | {0:*>8}'.format(11,12,13))

print('This is my ten-character, two-decimal number:{0:10.2f}'.format(13.579))



name='nidhi'
print(f'my name is {name}')

name='girl'
print(f"i'm {name!r}")


num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")
