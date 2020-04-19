# # blocks = int(input("Enter the number of blocks: "))
# # n =0
# # height=0
# # l = 0
# # while blocks:
# #     while n < blocks:
# #         print("row",n)
# #         while l != n:
# #             print("col",l)
# #             l +=1
# #             blocks -=1
# #         n +=1
# #         l=1
# #         blocks -=2

# #     else:
# #         break
# # # print(lowerLayer)
# # print("The height of the pyramid:",n)


# # count = 0
# # c0 = int(input("a number not 1:"))


# # if c0 % 2 == 0:
# #     c0 = c0 / 2
# # else:
# #     c0 = 3 * c0 + 1

# # while c0 != 1:
# #     print(int(c0))
# #     count +=1
# #     if c0 % 2 == 0:
# #         c0 = c0 / 2
# #     else:
# #         c0 = 3 * c0 + 1    
# # else:
# #     print(int(c0))
# #     count +=1


# # print("steps:",count)    

# # i=0
# # while i<=3:
# #     i+= 2

# #     # if i%2==0:
# #     #     break
# #     print("c")

# # lst1 =[1,2,3]
# # ls2 = []
# # for v in range(len(lst1)):
# #     lst1.insert(0,lst1[v])

# # print(lst1)

# # for i in range(1):
# #     print("d")
# # else:
# #     print("s")    

# # var=1
# # while var <10:
# #     print("#")
# #     var= var <<1

# # nums = [1,2,3]
# # vals= nums[-1:-2]

# # print(nums)
# # print(1/2+3//3+4**2)

# # x=2
# # y=4
# # x = x// y
# # # x = x%0 y
# # y = y// x
# # print(y)

# def isYearLeap(year):
#     if year % 4 == 0:
#         # return True
#         if year % 100 == 0:
#         # return False
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def daysInMonth(year, month):
#     oddMos =[1,3,5,7,8,10,12]
#     evenMos =[2,4,6,9,11]
#     days=0
#     if month in oddMos:
#         days =31
#     elif month in evenMos:
#         if month == 2:
#             if isYearLeap(year):
#                 days = 29
#             elif not isYearLeap(year):
#                 days = 28
#         else:
#             days= 30
#     else:
#         days = None

#     return days

# def dayOfYear(year, month, day):
#     a=0
#     for n in range(1,month):
#         res = daysInMonth(year,n)
#         a += res
#         print(res , "month:", n)
#     a += (daysInMonth(year,month) - day)
#     return a

# print(dayOfYear(2000, 1, 30))

# # testYears = [1900, 2000, 2016, 1987]
# # testMonths = [2, 2, 1, 11]
# # testResults = [28, 29, 31, 30]
# # for i in range(len(testYears)):
# # 	yr = testYears[i]
# # 	mo = testMonths[i]
# # 	print(yr, mo, "->", end="")
# # 	result = daysInMonth(yr, mo)
# # 	if result == testResults[i]:
# # 		print("OK",result,testResults[i])
# # 	else:
# # 		print("Failed")
# # 		print("OK",result,testResults[i])
# def fun(inp=2, out =3):
#     return inp * out

# print(2**2)
# print("````")

# tup= (1,2,4,8)
# tup = tup[-2:-1]
# tup= tup[-1]
# print(tup)
# print("````")

# def func(a):
#     if a%2==0:
#         return 1
#     else:
#         return
# print(func(func(2)+1))

# dct={}
# lst=['a','b','c','d']
# for i in range(len(lst)-1):
#     dct[lst[i]] = (lst[i],)
# for i in sorted(dct.keys()):
#     k=dct[i]
#     print(k[0])

# def funct1(a):
#     return None

# def funct2(a):
#     return funct1(a) * funct1(a)

# # print("hg",funct2(2))

# dct= {
#     'one':'two',
#     'three':'one',
#     'two':'three',
# }
# v= dct['three']

# for k in range(len(dct)):
#     v= dct[v]

# print(v)

# l=[0 for i in range(1,3)]
# print(l)

# var= 0
# while var < 6:
#     var+=1
#     if var % 2==0:
#         continue
#     print("df")

# vals=[0,1,2]
# vals.insert(0,1)
# del vals[1]
# print(vals)

# d= [1,2,3]
# for v in range(len(d)):
#     d.insert(1,d[v])
# print(d)

# x= 1/2+3//3+4**2
# print(x)

# x= 3
# y = 2
# # x= x/y
# # y= y/x
# # print(y)
# x= x%y
# x= x%y
# y= y%x
# print(y)

# x= 1//5+1/5
# print(x)

# lst = [i for i in range(-1,-2)]
# print(lst)

# def fun(x,y):
#     if x== y:
#         return x
#     else:
#         return fun(x,y-1)
# print(1//2)


# lst = [[x for x in range(3)] for y in range(3)]
# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 !=0:
#             print("f")
# print(lst)

# dct={}
# dct['1']= (1,2)
# dct['2'] = (2,1)

# for x in dct.keys():
#     print(dct[x][1],end="")
# print("````")
# nums= [1,2,3]
# vals = nums
# del vals[:]

# print(nums)
# print(vals)
# print("````")

# tup

from platform import processor

print(processor())