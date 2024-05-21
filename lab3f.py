#!/usr/bin/env python3

# Place my_list below this comment (before the function definitions)
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # Appends a new item to the end of the list with the value (last item + 1)
    if ordered_list:
        ordered_list.append(ordered_list[-1] + 1)
    else:
        ordered_list.append(1)

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all values found in items_to_remove list from ordered_list
    ordered_list[:] = [item for item in ordered_list if item not in items_to_remove]

# Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1, 5, 6])
    print(my_list)

