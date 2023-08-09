import sys


def caesar_swap(source, character, key):
    index = source.index(character)
    index = (index + key) % len(source)
    return source[index]


def encrypt_msg(msg, key, encrypt_numbers=False):
    upper_alphabet = [chr(i) for i in range(65, 91)]
    lower_alphabet = [chr(i) for i in range(97, 123)]
    numbers = "0123456789"

    new_msg = ""

    for i in msg:
        if i in upper_alphabet:
            new_msg += caesar_swap(upper_alphabet, i, key)
        elif i in lower_alphabet:
            new_msg += caesar_swap(lower_alphabet, i, key)
        elif i in numbers and encrypt_numbers:
            new_msg += caesar_swap(numbers, i, key)
        else:
            new_msg += i
    return new_msg


def decrypt_msg_brute(msg, dict_source, decrypt_numbers=False):
    letters = len([chr(i) for i in range(97, 123)])
    correct_key = 0

    dictionary = open(dict_source, "r")
    terms = dictionary.readlines()

    for term in range(len(terms)):
        terms[term] = terms[term][:-1]

    dictionary.close()
    split_msg = msg.split(" ")

    iter = 0

    for word in split_msg:
        iter += 1
        if len(word) > 3:
            for i in range(letters):
                iter += 1
                if encrypt_msg(word.strip(), i, decrypt_numbers) in terms:
                    correct_key = i
                    break

    return encrypt_msg(msg, correct_key, decrypt_numbers)


def save_result(msg, path):
    output_file = open(path, "w")
    output_file.write(msg)
    output_file.close()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("""
Caesar's Cypher Encrypter/Decrypter
              
    -msg '[YOUR MESSAGE]'   | Input text
    -k or -key KEY          | Key for the cypher
    -f '[PATH]'             | Input text from file
    -o '[PATH]'             | File for storing the output
    -d                      | Set program to decrypt a message through brute force, requires -dict
    -dict '[PATH]'          | Path to txt file, used as a dictionary for the brute force decrypting
    -n                      | Shift numbers along with letters
    -noprint                | Turn off the printing of results
    
    EXAMPLES:
        python caesar.py -msg 'This is an example.' -k 6
        python caesar.py -f input.txt -k -5 -o output.txt
        
        python caesar.py -msg 'This is an example of decrypting. You could also use -f for getting text from a file.' -d -dict dictionary.txt
""")
        sys.exit()

    if "-key" in sys.argv:
        key = int(sys.argv[sys.argv.index("-key") + 1])
    elif "-k" in sys.argv:
        key = int(sys.argv[sys.argv.index("-k") + 1])
    print_result = not "-noprint" in sys.argv

    new_msg = ""
    output_file_path = ""
    write_result = False
    decrypt = "-d" in sys.argv
    source_dict = ""
    change_numbers = "-n" in sys.argv

    if decrypt:
        if "-dict" in sys.argv:
            source_dict = sys.argv[sys.argv.index("-dict") + 1]
        else:
            raise Exception("No dictionary was specified. Use '-dict' to specify a dictionary in .txt format.")

    if "-f" in sys.argv:
        file_path = sys.argv[sys.argv.index("-f") + 1]
        file = open(file_path, "r")
        msg = file.read()
        file.close()
    else:
        msg = sys.argv[sys.argv.index("-msg") + 1]

    if "-o" in sys.argv:
        output_file_path = sys.argv[sys.argv.index("-o") + 1]
        write_result = True

    if not decrypt:
        new_msg = encrypt_msg(msg, key, change_numbers)
    else:
        new_msg = decrypt_msg_brute(msg, source_dict, change_numbers)

    if write_result:
        save_result(new_msg, output_file_path)
    
    if print_result:
        print(new_msg)
