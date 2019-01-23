# TextProcessor

## Part A
A program that takes a text file as a command line argument and outputs the word frequency in decreasing order.

It implements the following functionality:
1. Read an input file passed as a command line argument
2. Tokenize the text of the file. A token is a sequence of alphanumeric characters (a-zA-Z0-9), independent of capitalization (so “Apple” and “apple” are the same token)
3. Counts the number of occurrences of each word in the tokens generated
4. Print out the word frequency counts onto the screen. The print out should be ordered by decreasing frequency. (so, highest frequency words first). Resolve ties alphabetically in ascending order.
5. It reads the file line by line so it can handle large files.

## Part B
A program that takes two text files as arguments and outputs the number of tokens they have in common. Here is an example:

**Input file 1:**
We reviewed the trip and credited the cancellation fee. The driver has been notified.

**Input file 2:**
If a trip is cancelled more than 5 minutes after the driver-partner has confirmed the request, a cancellation fee will apply.

**Output**
6

## How to use
### Part A
`python PartA.py test1.txt`

`test1.txt` can be any text file of your choice, just make sure it's in the same folder as PartA.py.

### Part B
`python PartB.py test1.txt test2.txt`

`test1.txt` and `test2.txt` can be any text file of your choice, just make sure it's in the same folder as PartA.py.
