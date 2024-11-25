def main():
    bookpath = "books/frankenstein.txt"
    text = get_book_text(bookpath)
    number_of_words = get_num_words(text)
    chars_dict = get_num_char(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the document")
    
    result = reporting(chars_dict)
    print(result)
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

def reporting(my_dict):
    sorted_items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = dict(sorted_items)

    for key, value in sorted_dict.items():
        if key.isalpha() and key != " ":
            print(f"The '{key}' character was found {value} times")
        else:  
            None

    # return(sorted_dict)

main()
