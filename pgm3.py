color=input("Enter colors Sepreated by comma(,):")
color_list1=color.split(',')
print("First Color:",color_list1[0])
print("Second Color:",color_list1[-1])
color_list2=["Red","Orange","Black","White"]
print("Color-List1 not Contained in List2")
diff=list(set(color_list1)-set(color_list2))
print(diff)
color_int_list=[]
for color in color_list1:
    color_int_list.append(len(color))
print(f"List of integers corresponding to each color:{color_int_list}")