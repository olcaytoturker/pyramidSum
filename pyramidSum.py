def isNotPrime(num):



 if num==1:

   return True

 else:

     for i in range(2,num):

         if num%i==0:
             return True



     return False


with open("ffff.txt", "r") as f:

    sum = 0
    i=0
    index=0
    for line in f:


        nums=line.split()
        if i==0:
         sum+=int(nums[0])
         i=1

        else:

         if(int(nums[index]) > int(nums[index+1]) and isNotPrime(int(nums[index]))):

          sum+=int(nums[index])

         else:

          index=index+1
          sum+=int(nums[index])





    print(sum)