#Code in this cell
st = 'Create a list of the first letters of every word in this string'
sec_lis = [y for y in st.split(" ")]
print(sec_lis)
for item in sec_lis:
    print(item[0])