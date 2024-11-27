day= int(input("Enter Day:"))
mon= int(input("Enter a Month:"))
year= int(input("Enter a year:"))
print(f"{day}--{mon}--{year}")
if(year%4==0 and year%100!=0) or(year%400==0):
  print(f"{year} is leap year")
else:
  print(f"{year}  not is leap  year")
