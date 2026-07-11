#method-1
def func(count):
    if count == 5:
        return
    print("Manogna")
    func(count + 1)
func(0)


#method-2
count = 0
def func():
    global count
    if count == 5:
        return
    print("Manogna")
    count +=1 
    func()
func()
