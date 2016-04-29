import math
print('You can choose the graph as below:\na.rectangle\nb.square\nc.circular\nd.sector\ne.triangle\n')
def graph():
        a='rectangle'
        b='square'
        c='circular'
        d='sector'
        e='triangle'
temp=raw_input('Please enter the name of the graph:')
graph=str(temp)
if graph=='e':
   side1,side2,side3=input('Please enter three sides of the triangle:')
   side1,side2,side3=float(side1,side2,side3)
   while side1<=0 or side2<=0 or side3<=0:  
       while side1<=0 or side2<=0 or side3<=0:
             side1,side2,side3=input('The number is illegal,please enter again:')
       else:
           if side1>side2:
              a=side2
              side2=side1
              side1=a
           else:
               if side1>side3:
                  b=side3
                  side3=side1
                  side3=side1
               else:
                   if side2>side3:
                      c=side3
                      side3=side2
                      side2=c
                   else:
                       if (side1+side2)<=side3:
                           side1,side2,side3=input('The number three sides can not build a triangle,please enter again:')
p=(side1+side2+side3)/2
print('The perimeter of the graph is %.2f'%(side1+side2+side3))
print('The area of the graph is %.2f'%(math.sqrt(p*(p-side1)*(p-side2)*(p-side3))))        



