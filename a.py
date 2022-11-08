n = int(input('enter the number of data :'))
sum = 0

for i in range(n):
    data = int(input('Enter an integer :'))
    sum += data
print('The average of', n , 'numbers is', sum/n)



#### Exercise 4
num = int(input('Enter the number of integer: '))
data = []

for i in range(num):
    data.append(int(input('Enter the number of data : ')))


# define finmax function
def findmax(data):
    find = 0
    find = max(data)
    return find

#define selectionSort function
def selectionSort(data):
    data.sort(reverse = True)
    return data


print('findmax :', findmax(data))
print('sort_decending:', selectionSort(data))