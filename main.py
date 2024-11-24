def main():
    bookpath = "books/frankenstein.txt"
    text = get_book_text(bookpath)
#    print(text)
    number_of_words = get_num_words(text)
    chars_dict = get_num_char(text)

    print(f"{number_of_words} words found in document")
    print(f"\nAantal characters in text:\n {result} ")
   
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

main()



