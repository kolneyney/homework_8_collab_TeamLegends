
def index_power(numbers, n):

    try:

        index_number=numbers[n]
        result= index_number**n
        
    except IndexError:
        return -1
    

    return result



def main():
        numbers= list(map(int, input("Input numbers:").split(' ')))
        n= int(input('Input index number:'))
    
if __name__ == '__main__':
    main()