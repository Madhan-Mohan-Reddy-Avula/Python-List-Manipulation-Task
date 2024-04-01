class ListManipulator:
    def __init__(self):
        self.internal_list = []

    def add_elements(self, elements):
        self.internal_list.extend(elements)

    def remove_duplicates(self):
        self.internal_list = list(set(self.internal_list))

    def reverse_list(self):
        self.internal_list.reverse()

    def sort_list(self):
        self.internal_list.sort()

    def get_unique_elements(self):
        return list(set(self.internal_list))

    def remove_element(self, element):
        if element in self.internal_list:
            self.internal_list.remove(element)

    def get_list(self):
        return self.internal_list

# Example usage:
lm = ListManipulator()
lm.add_elements([1, 2, 3, 4, 2, 3, 5])
print("Original List:", lm.get_list())
#List after removing duplicates
lm.remove_duplicates()
print("List after removing duplicates:", lm.get_list())
#Reversed List
lm.reverse_list()
print("Reversed List:", lm.get_list())
#Sorted List
lm.sort_list()
print("Sorted List:", lm.get_list())
#Unique Elements
unique_elements = lm.get_unique_elements()
print("Unique Elements:", unique_elements)
#List after removing element
lm.remove_element(3)
print("List after removing element 3:", lm.get_list())