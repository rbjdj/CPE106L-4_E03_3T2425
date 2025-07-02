import stats
l = [1,3,2,2,1,1,5,5,5,5,4,4,4]
print("List = ", l)
print("Median = ", stats.median(l))
print("Mode = ", stats.mode(l))
print("Mean = ", stats.mean(l))

def median (l):
   if not l:
       return 0
   l.sort()
   lngth = len(l)
   if lngth % 2 == 0:
       return (l[(lngth//2)-1])
   else:
       return (l[lngth//2])
def mode (l):
   if not l:
       return 0
   dictionary = {}
   for num in l:
       number = dictionary.get(num, None)
       if number == None:
           dictionary[num] = 1
       else:
           dictionary[num] = number + 1
   theMax = max(dictionary.values())
   for key in dictionary:
       if dictionary[key] == theMax:
           return (key)
def mean (l):
   if not l:
       return 0
   return (sum(l) / len(l))
