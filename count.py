def most_frequent(string):
   
    freq = {}
    
    for letter in string:
        freq[letter] = freq.get(letter, 0) + 1
    
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    for item in sorted_freq:
        print(f"{item[0]} = {item[1]:02d}")


string = input("Please enter a string: ")
print("Output:")
most_frequent(string)
