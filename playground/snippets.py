def for_loop_using_slice_to_copy_array(words=[]):
    for word in words[:]:  # Loop over a slice copy of the entire list.
        if len(word) > 6:
            words.insert(0, word)


def array_with_elements_in_sequential_order(max=10):
    return list(range(max))


def create_array_with_random_values_of_size(size=1, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]
