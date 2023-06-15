
#->Number of occurrences of each letter present in the string in Dictionary . aabbcdeaabbceder
group="aabbcdeaabbceder"
list1=[]
for i in group:
    list1.append(i)
set1=set(list1)
print(set1)
new_list=sorted(list(set1))
for char in new_list:
      print(char, " appeared ",list1.count(char)," times.")

