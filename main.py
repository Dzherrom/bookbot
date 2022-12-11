# reads a book and print it into 
# console

path = 'books/frankenstein.txt'

def run():
    text = get_text(path)           #gets text
    words = get_words(text)         #counts words 
    characters_dictionary = get_letters(text)       #counts letters
    char_dict_to_list = letters_to_sorted_list(characters_dictionary) #turns dict into list

    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")

    for item in char_dict_to_list: #for loop to print letters as report
        if item["char"].isalpha() == True: #conditional uses isalpha to only print letters
            print('The',{item['char']},' character was found ',{item['num']},' amount of times')
    print('--- End of the report ---') 


# gets file text
def get_text(path):
    with open(path) as f:
        return f.read()

# returns num in letters to sorted list
def sort_on(d):
    return ["char"]

# sorts the number of characters dict into a list
def letters_to_sorted_list(characters_dictionary):
    new_list = []
    for c in characters_dictionary: # For loop appends character key and number key into list
        new_list.append({"char": c, "num": characters_dictionary[c]})
    new_list.sort(reverse = False, key=sort_on) # Sorts list using func parameter
    return new_list

# counts words
def get_words(text):
    words = text.split()
    count = len(words)

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
  

if __name__ == '__main__':
    run()