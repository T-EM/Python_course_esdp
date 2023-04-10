# slicing
a = "Hello"
print(a[1:4])

# # slice from start
b = "Hello"
print(b[:4])

# # slice from end
c = "Hello"
print(c[3:])

# # skipping slicing
c = "Hello world"
print(c[::1])
print(c[::2])
print(c[::-1])

# Upper case
d = "moHaN"
print(d.upper())

# Lower case
e = d
print(e.lower())

# Remove whitespace (Replace)
f = "Hey Buddy how is going"
print(f.replace(' ', ''))

# split strings
g = "Hey Buddy how is going"
print(f.split(' '))

# strip strings
h = "'Hey Buddy how is going                  '"
print(h.strip())

# # # # # LIST # # # # #

# Indexing
lis = ["no", "where", "there"]
print(lis[1])

# slicing
lis = ["no", "where", "there"]
print(lis[2:5])

# Reverse Indexing
lis = ["no", "where", "there"]
print(lis[-1])

print()
# Inserting items in list
lis = ["no", "where", "there"]
print(len(lis))
print(lis)
lis.insert(3, "go")
print(len(lis))
print(lis)

# Append items in list
lis = ["no", "where", "there"]
print(len(lis))
print(lis)
lis.append("here")
print(len(lis))
print(lis)

# pop items from list
lis = ["no", "where", "there"]
print(len(lis))
print(lis)
lis.pop()
print(len(lis))
print(lis)