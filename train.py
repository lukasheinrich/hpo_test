import json
import sys

def evaluate(x,y):
    return (x-1)**2 + (y-3)**2

def main():
   pars = json.load(open(sys.argv[1]))
   result = evaluate(**pars)
   json.dump({'result': result},open(sys.argv[2],'w'))

    

if __name__ == '__main__':
    main()
