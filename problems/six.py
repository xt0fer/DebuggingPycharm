import sys

def magic(x, y):
    return x + y * 2

if __name__ == "__main__":
    x = sys.argv[1]
    y = sys.argv[1]

    answer = magic(x, y)

    print('The answer is: {}'.format(answer))

## Suppose that we run this script with the inputs 1 and 50 expecting the result 101.

# $ python3 six.py 1 50
