def main():
    bookpath = "books/frankenstein.txt"
    text = get_book_text(bookpath)
    number_of_words = get_num_words(text)
    chars_dict = get_num_char(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the document\n")
    reporting(chars_dict)

    
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    lowered_text = text.lower()
    my_dict = {}
        
    for letter in lowered_text:
        if letter in my_dict.keys():
            my_dict[letter] += 1
        else:
            my_dict.update({letter : 1})
    return my_dict    


def sort_on(VAR):
    return VAR["num"]

def reporting(my_dict):
    #sorted_items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    #sorted_dict = dict(sorted_items)
    sorted_list = []
    for char, count in my_dict.items():
        if char.isalpha() and char != " ":
            char_dict = {"char" : char, "num" : count}
            sorted_list.append(char_dict)
    sorted_list.sort(reverse=True, key=sort_on)
#sort_on (correct) - gives Python the function to use
#sort_on() (incorrect) - tries to run the function right away with no arguments
#sort_on(VAR) (incorrect) - tries to run the function right away with VAR
#call the function, not a value, so sort_on and not sort_on()
            
            #print(f"The '{char}' character was found {count} times")
    for item in sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")



main()
