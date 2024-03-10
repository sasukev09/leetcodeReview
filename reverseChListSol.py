# Write a function that reverses the string. The input string is given as an array of characters.
# Must do this by modifying the input array in-place with O(1) extra memory.

# Creating the list that we want to reverse
name_as_list = ["k", "e", "v"]


# Creating the class that will contain the method that gives the solution
class Solucion(object):
    def reverseStringList(self, ch):
        s, e = 0, len(ch) - 1
        while s <= e:
            temp = ch[s]
            ch[s] = ch[e]
            ch[e] = temp
            s = + 1
            e = - 1


# Creating an instance of the Solucion class
Solucion = Solucion()


# Print list before reversing
print(name_as_list)


# Apply method from Solucion class to the list
Solucion.reverseStringList(name_as_list)


# Print result from the reverse list method
print("The reversed list is:", name_as_list)
