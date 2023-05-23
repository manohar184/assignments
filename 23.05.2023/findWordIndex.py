text = 'manohar is a good boy and manohar is intelligent'
index = 0
while index < len(text):
    index = text.find('manohar', index)
    if index == -1:
        break
 
    print(index, end=" ")
    index += 7 