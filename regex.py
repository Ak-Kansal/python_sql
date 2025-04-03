import re
# k="the rain in spain"
# x=re.search("^the.*spain$",k)
# # ^ to check the starting
# # .* to check any character
# # $ to check the ending
# if(x):
#     print("yes")
# else:
#     print("no")
# i=re.findall("ai",k)
# if(i):
#     print("yes")
# else:
#     print("no")
# st="this, is , a , string for split, function"
# s=re.split(",",st)
# print(s)
# t=re.sub(",","22",st,2)
# print(t)

# pat="^aks.*kansal$"
# s="akshay kansal"
# if(re.match(pat,s)):
#     print("yes")
# else:
#     print("no")

line="akshat@123.com"
email=re.findall(r'[\w\.-]+@[\w\.-]+(\.)+[\w]+',line)
fixedlength=re.findall(r'[\w\.-]+@[\w\.-]+(\.)+[\w]{2,4}$',line)
if(fixedlength):
    print("yes")    
else:   
    print("no")