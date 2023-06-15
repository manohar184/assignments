group="aabbcdeaabbceder"
list1=[]
for i in group:
    list1.append(i)
set1=set(list1)
print(set1)
new_list=sorted(list(set1))
vowel_list1=["a","e","i","o","u"]
vowel_list2=[]
for char in new_list:
     if char in vowel_list1:
          vowel_list2.append(char)
          

for char in vowel_list2:
      print(char, " appeared ",list1.count(char)," times.")
