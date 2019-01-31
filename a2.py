# Name:           Brandom Gillespie
# Student Number: A00966847
# Class:          COMP7402
# Assignment:     A2
# Purpose: The purpose of this program is to break a transposition cipher. The
# ciphertext can be given as either a file or through keyboard input. This implementation
# uses the DetectEnglish python file to analyze the potential plaintext for decryted text
# analysis.
import sys, detectEnglish, math

def decryptMessage(key, message):
    # Determine the number of columns
    nCols = math.ceil (len (message) / key)
    # Determine the number of rows
    nRows = key
    # Determine the unused cells
    nUnused = (nCols * nRows) - len(message)
    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * nCols
    # row and col point to the location of the next character in the ciphertext
    row = col = 0
    for symbol in message:
        plaintext[col] += symbol
        col += 1 # point to next column

        # If it reaches the last column in the row, or at an unused cell, start processing the next row
        if (col == nCols) or (col == nCols - 1 and row >= nRows - nUnused):
            col = 0
            row += 1
    return ''.join(plaintext)

# Main
def main():
    # Get source of ciphertext from user
    ciphertext = ""
    while (True):
        where_is_cipher = input("Is the ciphertext given via stdin or file? ")
        if where_is_cipher == "file":
            print("File selected")
            cipher = input("File name please: ")
            ciphertext += open(cipher, 'rU').read()
            print(ciphertext)
            break
        elif where_is_cipher == "stdin":
            print("stdin selected")
            cipher = input("Ciphertext name please: ")
            ciphertext = cipher
            print(ciphertext)
            break
        else:
            print("Need to select a valid option ('file' or 'stdin')")

    # Decrypt and test
    for k in range(len(ciphertext) - 1):
        print("Testing Key: %d" % (k + 1))
        plaintext = decryptMessage(k + 1, ciphertext.strip('\n'))
        if detectEnglish.FindEnglish(plaintext):
            print()
            print("Found Potential Key: %d" % (k + 1))
            print(plaintext)
            check = input("Does this plaintext make sense: (y/n) ")
            if check == "y":
                print()
                print("Key is: %d" % (k + 1))
                print("Plaintext is: %s" % plaintext)
                print()
                sys.exit()
            else:
                print("Continuing")
                print()

# Main
if __name__ == "__main__":
    main()
