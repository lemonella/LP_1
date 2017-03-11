'''
weather = {'temperature':'10', 'city':'Moscow'}
print(weather)

if __name__ == '__main__':
	print('I was called from the shell')
'''

def myfunc(x, y):
	return(str(x) + ' ' + str(y))

print(myfunc(input('x: '), input('y: ')))
words = myfunc(input('x: '), input('y: '))
print(words.upper())