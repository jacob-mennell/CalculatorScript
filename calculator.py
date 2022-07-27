def calculator():
    """
    Function loads instructions from input.txt file and returns an output number to the screen.
    Instructions comprise a lower case keyword and a number that are separated by a space per line.

    Instructions: 'add', 'subtract', 'multiply', 'divide', 'apply'

    The last instruction should be "apply" and a number (e.g., "apply 3").
    The calculator is then initialised with that number and the previous instructions are applied to that number.

    Example:
    [Input from file]
    add 2
    multiply 3
    apply
    [Output to screen]
    15

    :return: float

    """

    with open('input.txt') as f:
        num_list = []
        ops_list = []

        # loop through text file and append instructions and number to lists
        for line in f:
            try:
                words = line.split()
                num_list.append(int(words[1]))
                ops_list.append(words[0])
            except Exception as e:
                print(e)

    # last number to initialise the calculator
    result = num_list[-1]

    # perform calculations based on instructions
    for x in range(len(num_list)-1):
        if ops_list[x] == 'add':
            result = result + num_list[x]
        elif ops_list[x] == 'subtract':
            result = result - num_list[x]
        elif ops_list[x] == 'multiply':
            result = result * num_list[x]
        elif ops_list[x] == 'divide':
            result = result / num_list[x]
        else:
            raise ValueError("Unknown operation listed")

    return result
