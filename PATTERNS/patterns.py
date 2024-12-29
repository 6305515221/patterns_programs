

##oddnumbrs:-(2*i-1) like 1,3,5,7,9
##7,5,3,1:-(2*n-2*i+1)
##< or > we use (2*n-i)
#(2*(i-1)-1)


'''
5
* * * * * 
* * * * 
* * * 
* * 
*

n=int(input())
for i in range(n):
    print('* '*(n-i))

#or
for i in range(n,0,-1):
    print('*'*i)

n=int(input())
sp=0
s=n
for i in range(n):
    for j in range(sp):
        print(' ',end=' ')
    for k in range(s):
        print("*",end=' ')
    s-=1
    print()
'''


####
'''

    *
   **
  ***
 ****
*****

for i in range(1,n+1):
    print(f"{i*' *':>15}")
'''
'''
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
n=int(input())
for i in range(1,n+1):
    print("  "*(n-i)+"* "*i)

'''
######
'''
       *       
      * *      
     * * *     
    * * * *    
   * * * * *   
n=int(input())
for i in range(1,n+1):
    print(f"{i*' *':^15}")
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
'''
'''
5
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
n=int(input())
for i in range(n):
    print(' '*i+"* "*(n-i))
'''

#we donot use space
'''
*****
 ****
  ***
   **
    *
n=int(input())
for i in range(n):
    print(f"{' '*i+"*"*(n-i)}")
'''
'''
* * * * 
  * * * 
    * * 
      *
      
n=int(input())
for i in range(1,n+1):
    print('  '*(i-1)+'* '*(n-i))
'''

'''
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
n=int(input())
for i in range(1,n+1):
    print('  '*(n-i)+"* "*(2*i-1))
'''


'''
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
n=int(input())
for i in range(1,n+1):
    space='  '*(2*n-(2*i))
    print('* '*i+space+'* '*i)

'''
#########
'''
5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

n=int(input())
s=''
for i in range(1,n+1):
    s+=str(i)+' '
    print(s)

n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
'''


'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5  5 
n=int(input())
for i in range(1,n+1):
    print((str(i)+' ')*i)




'''
    
'''
      1 
    2 2 2 
  3 3 3 3 3 
4 4 4 4 4 4 4 

n=int(input())
for i in range(1,n+1):
    print("  "*(n-i)+(str(i)+' ')*(2*i-1))

'''

#####
'''
     1 
    1 2 
   1 2 3 
  1 2 3 4 
 1 2 3 4 5

n=int(input())
s=' '
for i in range(1,n+1):
    s+=str(i)+' '
    print(' '*(n-i)+s)


n=int(input())
for i in range(1,n+1):
    print('  '*(n-i),end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()

'''

'''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
n=int(input())
for i in range(n):
    print((n-i)*(str(n-i)+' '))
'''


'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1

n=int(input())
for i in range(1,2*n):
    if(i<=n):
        print((str(i)+' ')*i)
    else:
        a=2*n-i
        print((str(a)+' ')*(2*n-i))

'''


'''
* * * * * 
+ + + + 
+ + + 
+ + 
+ 
n=int(input())
for i in range(n,0,-1):
    if(i==n):
        print("* "*i)
    else:
        print("+ "*i)
'''
'''
* 
* * 
* * * 
* * * 
* * 
* 

n=int(input())
for i in range(1,n+1):
    print('* '*i)
for i in range(n,0,-1):
    print('* '*i)
'''
######
'''
        #
      + #
    + + #
  + + + #
+ + + + #
  + + + #
    + + #
      + #
        #

n=int(input())
for i in range(1,2*n):
    if(i==1):
        print('  '*(n-i)+'#')
    elif(i<=n):
        print('  '*(n-i)+'+ '*(i-1)+'#')
    else:
        print('  '*(i-n)+'+ '*(2*n-i-1)+'#')
'''

        
    
###
'''
A 
A B 
A B C 
A B C D 
A B C D E

n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j),end=' ')
    print()

#or
s=''
for i in range(ord('A'),ord("F")):
    s=s+chr(i)+' '
    print(s)

'''


'''
         A 
       A B 
     A B C 
   A B C D 
 A B C D E
 
n = 5

for i in range(n):
    # Print leading spaces
    print(' ' * (2 * (n - i - 1)), end='')
    
    # Print letters
    for j in range(i + 1):
        print(chr(65 + j), end=' ')
    
    # Move to the next line
    print()

n=5
for i in range(1,n+1):
    print('  '*(n-i),end=' ')
    for j in range(i):
        print(chr(65+j),end=' ')
    print()
'''

#######
'''
         A 
       A C 
     A C E 
   A C E G 
 A C E G I
 
n=int(input())
for i in range(n+1):
    print('  '*(n-i),end=' ')
    for j in range(i):
        print(chr(65+2*j),end=' ')
    print()
'''
#####
'''
A B C D E F 
A B C D E 
A B C D 
A B C 
A B 
A

for i in range(6,0,-1):
    for j in range(i):
        print(chr(65+j),end=' ')
    print()
s=''
for i in range(5,0,-1):
    for j in range(i):
        s=chr(ord('a')+j)
        print(s,end=' ')
    print()
'''

####
'''
     A 
    A B 
   A B C 
  A B C D 
 A B C D E 

n=int(input())
for i in range(1,n+1):
    print(' '*(n-i),end=' ')
    for j in range(i):
        print(chr(65+j),end=' ')
    print()

s=''
for i in range(6):
    s+=chr(65+i)+' '
    print(' '*(6-i)+s)
'''
#######
'''
 *
 *
 *
 * *
 *
 * * *
 *
 * * * *
 *
 * * * * *
for i in range(1,6):
    print(' *')
    print(i*' *')

'''
#####
'''
        * 
      * * 
    *   * 
  *     * 
* * * * * 
n=int(input())
for i in range(1,n+1):
    if(i==1):
        print('  '*(n-i)+'* ')
    elif(i==n):
        print("* "*n)
    else:
        print('  '*(n-i)+'* '+'  '*(i-2)+'* ')
 '''
##tabe
'''
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i*j<10):
            print('0'+str(i*j),end=" ")
        else:
            print(i*j,end=' ')
    print()


output
5
01 02 03 04 05 
02 04 06 08 10 
03 06 09 12 15 
04 08 12 16 20 
05 10 15 20 25
'''


'''
         g
        gr
       gra
      gram
     gramp
    grampr
   grampro


n='program'
s=''
middle_value=n[len(n)//2]
middle_index=n.index(middle_value)
for i in range(middle_index,len(n)):
    s+=n[i]+' '
    print(s)
    if(i==len(n)-1):
        for j in range(middle_index):
            s+=n[j]+' '
            print(s)
'''

#####
'''
666666
655556
654456
654456
655556
666666

n=int(input())
for i in range(n):
    for j in range(n):
        value=min(i,j,n-i-1,n-j-1)+1
        print(n-value+1,end='')
    print()

'''

'''
4
1 2 3 4 
1 2 3 
1 2 
1
n=int(input())
for i in range(n+1,0,-1):
    for j in range(1,i):
        print(j,end=' ')
    print()
'''
'''
4
4444
333
22
1
n=int(input())
for i in range(n,0,-1):
    print(str(i)*i)
'''
########
'''
2
24
246
2468
246810

n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(2*j,end='')
    print()

       

n=int(input())
for i in range(1,n+1):
    print('  '*(n-i),end='')
    for j in range(i,0,-1):
        print(2*j,end='')
    print()
'''

#######
'''
246810
2468
246
24
2


n=int(input())
for i in range(n+1,1,-1):
    for j in range(1,i):
        print(str(2*j),end='')
    print()
'''

###########
'''
5
1 
1 3 10
1 3 5 
1 3 5 7 
1 3 5 7 9 
2 4 6 8 10 
2 4 6 8 
2 4 6 
2 4 
2 

n=int(input())
s=''
for i in range(1,2*n,2):
    s=s+str(i)+' '
    print(s)
for i in range(n+1,1,-1):
    for j in range(1,i):
        print(str(2*j),end=' ')
    print()

n=5
for i in range(1,(2*n)+1):
    if(i<=n):
        d=1
        for j in range(i):
            print(d,end=' ')
            d+=2
        print()
    else:
        d=2
        for k in range(2*n-i):
            print(d,end=' ')
            d+=2
        print()

'''


#########
'''
 ** ** 
*  *  *
*     *
 *   * 
  * *  
   * 
for i in range(6):
    for j in range(7):
        if(i==0 and j%3!=0) or (i==1 and j%3==0) or (i-j==2) or (i+j==8):
            print('*',end='')
        else:
            print(end=' ')
    print()
'''

'''
4
   *       * 
  * *     * * 
 * * *   * * * 
* * * * * * * * 
 * * * * * * * 
  * * * * * * 
   * * * * * 
    * * * * 
     * * * 
      * * 
       * 
n=int(input())#4
for i in range(1,3*n):
    if(i<=n):
        print(' '*(n-i)+'* '*(i)+' '*(n-i)+' '*(n-i)+'* '*(i))
    else:#5
        print(' '*(i-n)+'* '*(3*n-i))
'''

'''
5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
def pattern(n):
    for i in range(n):
        print('* '*n)
n=int(input())
pattern(n)

#or
for i in range(1,6):
    for j in range(1,6):
        print("* ",end=" ')
    print()
'''

######
'''
5
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5

def pattern(n):
    for i in range(1,n+1):
        print((str(i)+' ')*n)
n=int(input())
pattern(n)

#or
for i in range(1,6):
    for j in range(1,6):
        print(i,end=' ')
    print()

'''

'''
5
1 1 1 1 1 
3 3 3 3 3 
5 5 5 5 5 
7 7 7 7 7 
9 9 9 9 9 
def pattern(n):
    for i in range(1,n+1):
        print((str(2*i-1)+' ')*n)
n=int(input())
pattern(n)
'''
#####
'''
5
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
def pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(j,end=' ')
        print()
n=int(input())
pattern(n)
'''
#######
'''
5
1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 
21 22 23 24 25 
dummy=1
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()
'''
####
'''
5
A B C D E 
A B C D E 
A B C D E 
A B C D E 
A B C D E 
def pattern(n):
    for i in range(1,n+1):
        for j in range(n):
            print(chr(65+j),end=' ')
        print()
n=int(input())
pattern(n)
'''

#
'''
5
A A A A A 
B B B B B 
C C C C C 
D D D D D 
E E E E E 
def pattern(n):
    for i in range(n):
        for j in range(n):
            print(chr(65+i),end=' ')
        print()
n=int(input())
pattern(n)
'''

###
'''
5
A B C D E 
F G H I J 
K L M N O 
P Q R S T 
U V W X Y 
dummy=0
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(65+dummy),end=' ')
        dummy+=1
    print()
'''
###
'''
* ----
-* ---
--* --
---* -
----* 

n=int(input())
for i in range(1,n+1):
    #print('-'*(i-1)+'* '*1+'-'*(n-i))
    print('  '*(i-1)+'* '*1)

##or

n=int(input())
for i in range(n):
    for j in range(n):
        if(i==j):
            print('*',end=' ')
        else:
            print('-',end=' ')
    print()
###
'''
'''
----* 
---* -
--* --
-* ---
* ----

n=int(input())
for i in range(n,0,-1):
    print('-'*(i-1)+'* '*1+'-'*(n-i))
'''
##
'''
5
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 

n=int(input())
for i in range(1,n+1):
    print((str(i)+' ')*i)
'''

    
########
'''

5
1 
1 3 
1 3 5 
1 3 5 7 
1 3 5 7 9 
1 3 5 7 9 11 
n=int(input())
s=''
for i in range(n+1):
    s+=str(2*i+1)+' '
    print(s)
'''
'''
5
1 1 1 1 1 
  2 2 2 2 
    3 3 3 
      4 4 
        5

n=int(input())
for i in range(n):
    print('  '*(i)+(str(i+1)+' ')*(n-i))
'''

###
'''
5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 

n=int(input())
d=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(d,end=' ')
        d+=1
    print()
'''   
##13
'''
1 2 3 4 5 
  6 7 8 
    9 

d=1
for i in range(5,0,-2):
    print(' '*(5-i),end='')
    
    for j in range(i):
        print(d,end=' ')
        d+=1
    print()
'''
        

######
'''
pavan
p       p 
  a   a   
    v     
  a   a   
n       n 
n=input()
for row in range(len(n)):
    for col in range(len(n)):
        if(row==col or row+col==len(n)-1):
            print(n[row],end=' ')
        else:
            print(' ',end=' ')
    print()
'''
######
'''
pavan
p       n 
  a   a   
    v     
  a   a   
p       n 
n=input()
for row in range(len(n)):
    for col in range(len(n)):
        if(row==col or row+col==len(n)-1):
            print(n[col],end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
          A 
        B A B 
      C B A B C 
    D C B A B C D 
  E D C B A B C D E 
  E D C B A B C D 
    D C B A B C 
      C B A B 
        B A 



for i in range(1,6):
    print('  '*(6-i),end='')
    for j in range(i,0,-1):
        print(chr(65+j-1),end=' ')
    for k in range(1,i):
        print(chr(65+k),end=' ')
    print()
for a in range(4,0,-1):
    print('  '*(5-a),end='')
    for b in range(a,0,-1):
        print(chr(65+b),end=' ')
    for c in range(a):
        print(chr(65+c),end=' ')
    print()
'''
    
'''
E D C B A 
D C B A
C B A
B A
A

s=''
for i in range(5,0,-1):
    for j in range(i,0,-1):
        s=chr(64+j)
        print(s,end=' ')
    print()
        
'''
#####3
'''

        1 
      2 1 2 
    3 2 1 2 3 
  4 3 2 1 2 3 4 
5 4 3 2 1 2 3 4 5 
  4 3 2 1 2 3 4 
    3 2 1 2 3 
      2 1 2 
        1

n=int(input())
for i in range(1,n+1):
    print('  '*(n-i),end='')
    for j in range(i,0,-1):
        print(str(j)+' ',end='')
    for k in range(1,i):
        print(str(k+1)+' ',end='')
    print()

for h in range(n-1,0,-1):
    print('  '*(n-h),end='')
    for m in range(h,0,-1):
        print(m,end=' ')
    for o in range(2,h+1):
        print(o,end=' ')
    print()
'''
'''
        2 
      2 4 2 
    2 4 6 4 2 
  2 4 6 8 6 4 2 
2 4 6 8 10 8 6 4 2 


n=int(input())
for i in range(1,n+1):
    print('  '*(n-i),end='')
    for k in range(1,i):
        print(str(2*k)+' ',end='')
    for j in range(i,0,-1):
        print(str(2*j)+' ',end='')
   
    print()
'''
    
'''
1 1 1 1 1 
  2 2 2 2 
    3 3 3 
      4 4 
        5 

n=5
for i in range(1,n+1):
    print('  '*(i-1)+(str(i)+' ')*(n-i+1))
'''
'''
1 2 3 4 5 
  1 2 3 4 
    1 2 3 
      1 2 
        1 
n=5

for i in range(1,n+1):
    print('  '*(i-1),end='')
    d=1
    for j in range(n-i+1):
        print(d,end=' ')
        d+=1
    print()
'''

'''
1 2 3 4 5 
  6 7 8 9 
    10 11 12 
      13 14 
        15 

n=5
d=1
for i in range(1,n+1):
    print('  '*(i-1),end='')
    for j in range(n-i+1):
        print(d,end=' ')
        d+=1
    print()
'''
'''
A A A A A 
B B B B 
C C C 
D D 
E 
n=5
d=65
for i in range(1,n+1):
    #print('  '*(i-1),end='')
    
    for j in range(n-i+1):
        print(chr(d),end=' ')
        
    print()
    d+=1
'''


###
'''
                1 
              2 4 2 
            3 5 7 5 3 
          4 6 8 10 8 6 4 
        5 7 9 11 13 11 9 7 5 
          4 6 8 10 8 6 4 
            3 5 7 5 3 
              2 4 2 
                1 


n=9
sp=n-1
s=1
for i in range(n):
    d=(s//2)+1
    for k in range(sp):
        print(' ',end=' ')
    for c in range(s):
        print(d,end=' ')
        if(c<s//2):  #first side
            d+=2
        else:        ##second side
            d-=2
    if(i<n//2):  ##top code
        sp-=1
        s+=2
    else:      ##bottom code
        sp+=1
        s-=2
    print()
''' 
    
'''

        1
      2    2
    3        3
  4            4
5                5
  4            4
    3        3
      2    2
        1     

n=int(input())
for i in range(1,2*n):
    if(i==1 or i==2*n-1):
        print('  '*(n-1)+str(1))
    elif(i<=n):
        print('  '*(n-i)+str(i)+'  '*(2*i-2)+str(i))
    else:
        print('  '*(i-n)+str(2*n-i)+'  '*(2*(2*n-i)-2)+str(2*n-i))
'''










        
