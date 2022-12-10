# reads a book and print it into 
# console

path = 'books/frankenstein.txt'

def run():
    text = get_text(path)
    print(text)

def get_text(path):
    with open(path) as f:
     return f.read()
   

if __name__ == '__main__':
    run()