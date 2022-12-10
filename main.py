# reads a book and print it into 
# console

path = 'books/frankenstein.txt'

def run():
    text = get_text(path)
    words = get_words(text)
    characters_dictionary = get_letters(text)
    print("--- Begin report of ", path, ' ---')
    print(words, ' words were found in the document')

# gets file text
def get_text(path):
    with open(path) as f:
        return f.read()
   
# counts words
def get_words(text):
    words = text.split()
    count = len(words)
    return count

# counts letters 
def get_letters(text):
    
    characters = {
    }

    for w in text:
        minus = w.lower()

        if minus in characters:
            characters[minus] += 1

        else:
            characters[minus] = 1
    return(characters)
    
    # Turn dict into a list and print string with 
    # amount of times a letter was typed
    new_list = list(characters.items())
    return(new_list)
  

if __name__ == '__main__':
    run()