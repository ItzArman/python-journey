#Strings


#creating string
a = "hello, I'm Arman"
print(a)

#string slicing
a = "hyperium is op"
print(a[4])
print(a[0:8])

#check length
b = "sbwjwkans sbwja h2"
print(len(b))

print(b[0:18])

print(a[:78])

#advance slicing
#skipping character
d = "text here send plox"
print(d[::2])


#negative slicing
print(d[-4:])

#some advance string functions
print(d.find("here"))
print(d.capitalize())
print(d.replace("send", "ok"))
print(d.endswith("plox"))
print(d.count("e"))
print(d.upper())
