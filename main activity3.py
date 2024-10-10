from main1 import ArrayStack

stack = ArrayStack()
def reverse_file_lines(filename):
    """Reverses the lines of a file using a stack."""
    stack = ArrayStack()

    # Read lines from the file and push them onto the stack
    with open(filename, 'r') as file:
        for line in file:
            stack.push(line.rstrip('\n'))  # Remove newline characters

    # Pop the lines from the stack and write them back to the file
    with open(filename, 'w') as file:
        while not stack.is_empty():
            file.write(stack.pop() + '\n')  # Add newline when writing back

if __name__ == "__main__":
    filename = input("Enter the name of the file to reverse its lines: ")
    reverse_file_lines(filename)
    print(f"The lines in '{filename}' have been reversed.")

