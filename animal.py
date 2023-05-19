import sys

def dog():
    print('Baw')

def default():
    print('Hello')

def cat():
    print('Meow')

def main():
    if sys.argv[1] == 'dog':
        dog()
    elif sys.argv[1] == 'cat':
        cat()
    else:
        default()

if __name__ == '__main__':
    main()
