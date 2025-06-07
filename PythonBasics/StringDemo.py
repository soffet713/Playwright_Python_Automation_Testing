str = "RahulShettyAcademy.com"
str1 = "/Consulting_Firm"
beginning = "https://www."
str3 = "RahulShetty"

print(str[1]) # a

print(str[0:5]) # prints a substring "Rahul"

concatenated = str + str1
print(concatenated)

full_site_name = beginning + concatenated
print(full_site_name)

print(str3 in full_site_name)

# To remove white spaces, Python uses strip instead of trim. lstrip will remove only white space on left side.
# rstrip will remove only white space on the right side
str4 = "  great  "
print(str4)
print(str4.strip())
