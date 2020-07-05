# creating patent_no.txt
l = ['US3501303A','WO1994020294A1']
print(len(l))

file = open("test_link2.txt",'w')
# fields = ['Publication no']
# with open(filename, 'a') as file:
#     file.write()

for i in l:
     url = "https://patents.google.com/patent/" + i + "/en"
     file.write(url)
     file.write("\n")
     print(url)

print("Done")    