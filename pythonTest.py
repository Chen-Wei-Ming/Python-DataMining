arrayTest=["test" , "test2" , "test3"]
print('arrayTest :'+arrayTest[0])
print(arrayTest)
# get last
print(arrayTest.pop())
# add some element to last
arrayTest.extend(['test4' , 'test5'])
print(arrayTest)
arrayTest.insert(0 , 'test0')
print(arrayTest)
count = 0
for item in arrayTest:
    count = count + 1
    print(item)
    print(count)

count = 0
while  count < 10 :
    print(count)
    count = count + 1
# isinstance (object , class)
# if: else:
arrayList = ["test" , "test2"  ,["testlist1" , "testlist2"]]
print(arrayList)
for items in arrayList:
    if isinstance(items , list) :
        for item in items :
            print(item)
    else :
        print(items)

def printList(ListObject) :
    if isinstance(ListObject , list) :
        for Object in ListObject :
            print(Object)
    else :
        print(ListObject)

for Object in arrayList :
    printList(Object)

"""test something text for program"""
