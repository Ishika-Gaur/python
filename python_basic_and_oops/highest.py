def highest_even(li):
    even =[]
    for i in li :
        if i%2==0:
            even.append(i)
    return max(even)   

print(highest_even([4,84,3,11,23,45,67,89,90]))     
        