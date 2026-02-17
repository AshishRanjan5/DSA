def explore_swaps(digits_list, remaining_swaps, current_index, best_result):
    """
    Recursive helper function.
    It tries to create the maximum number by performing beneficial swaps.
    """

    # BASE CASE:
    # If no swaps are left OR we have reached the end of the list,
    # there is nothing more we can do, so return.
    if remaining_swaps == 0 or current_index == len(digits_list):
        return

    # Find the largest digit from the current position to the end.
    # We do this because placing the largest digit in front
    # always gives a larger number.
    largest_digit = max(digits_list[current_index:])

    # If the current digit is not already the largest,
    # then we must use one swap to improve the number.
    if digits_list[current_index] != largest_digit:
        remaining_swaps -= 1  # consume one swap

    # Loop from the end of the list back to current_index
    # so we try swapping with the rightmost largest digit first.
    for swap_position in range(len(digits_list) - 1, current_index - 1, -1):

        # Only swap if this position has the largest digit
        # (we do not want to swap with smaller digits)
        if digits_list[swap_position] == largest_digit:

            # Perform the swap to bring the largest digit forward
            digits_list[current_index], digits_list[swap_position] = (
                digits_list[swap_position],
                digits_list[current_index]
            )

            # Convert the list of digits back into a string
            # so we can compare it with the best number found so far
            current_number = "".join(digits_list)

            # If this new number is greater than the stored best result,
            # update the best result
            if current_number > best_result[0]:
                best_result[0] = current_number

            # Recursively process the next position
            # with the remaining swaps
            explore_swaps(digits_list, remaining_swaps, current_index + 1, best_result)

            # BACKTRACK STEP:
            # Undo the swap so that we can try a different swap
            # in the next loop iteration
            digits_list[current_index], digits_list[swap_position] = (
                digits_list[swap_position],
                digits_list[current_index]
            )


def find_maximum_number(digit_string, max_swaps):
    """
    Main function.
    This is the function that should be called from main().
    """

    # This list stores the best (maximum) number found so far.
    # We use a list so that it can be modified inside recursion.
    best_result = [digit_string]

    # Convert the string into a list because strings are immutable in Python,
    # and we need to swap characters.
    digits_list = list(digit_string)

    # Start recursive exploration from index 0
    explore_swaps(digits_list, max_swaps, 0, best_result)

    # After recursion finishes, best_result[0] contains the answer
    return best_result[0]


# second solution
def swap_chars(char_list, i, j):
    char_list[i], char_list[j] = char_list[j], char_list[i]


def find_max_number_optimal(number_string, max_swaps):
    digits = list(number_string)
    best_result = [number_string]
    backtrack(digits, max_swaps, best_result)
    return best_result[0]


def backtrack(digits, remaining_swaps, best_result):
    current_number = "".join(digits)

    if current_number > best_result[0]:
        best_result[0] = current_number

    if remaining_swaps == 0:
        return

    length = len(digits)

    for i in range(length):
        for j in range(i + 1, length):
            if digits[j] > digits[i]:
                swap_chars(digits, i, j)
                backtrack(digits, remaining_swaps - 1, best_result)
                swap_chars(digits, i, j)  # backtrack


if __name__=="__main__":
    print(find_maximum_number("129", 1))
    print(find_max_number_optimal("129", 1))
