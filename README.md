# Caesar's Cypher
A command line implementation in Python of the Caesar's Cypher cryptography algorithm. Includes encryption and brute force decryption of text passed through the terminal or text files.

## Pre-requisites
- pytest | For tests

## Installing
```git
git clone https://github.com/rafaelsalb/caesars-cypher
```
For decryption, have a text file in the following format:
```
word1
word2
word3
```
You can use [this](https://github.com/dwyl/english-words/blob/master/words_alpha.txt) dictionary.

## Usage
```
python caesar.py
```
This will show you how to use the tool.

### Examples
```python
python caesar.py -msg 'This is an example.' -k 6 # for encrypting a message from the terminal.
python caesar.py -f input.txt -k -5 -o output.txt # for encrypting a message from a file.

python caesar.py -msg 'This is an example of decrypting. You could also use -f for getting text from a file.' -d -dict dictionary.txt
