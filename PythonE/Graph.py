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
while graph != 'quit':
    if graph=='a':
       l,w=input('Please enter the length and width of the rectangle:')
       while l<=0 or w<=0:
          l,w=input('The number is illegal,please enter again:')
       print('The perimeter of the rectangle is %.2f'%(2*l+2*w))
       print('The area of the rectangle is %.2f'%(l*w))
    else:
        if graph=='b':
           l=input('Please enter the length of the square:')
           while l<=0:
              l=input('The number is illegal,please enter again:')
           print('The perimeter of the square is %.2f'%(4*l))
           print('The area of the square is %.2f'%(l*l))
        else:
            if graph=='c':
               r=input('Please enter the radius of the circular:')
               while r<=0:
                   r=input('The number is illegal,please enter again:')
               print('The perimeter of the circular is %.2f'%(2*math.pi*r))
               print('The area of the circular is %.2f'%(math.pi*r*r) )
            else:
                if graph=='d':
                   r,n=input('Please enter the radius and angle of the sector:')
                   while r<=0 or n<0:
                       r=input('The number is illegal,please enter again:')
                   l=n*math.pi*r/180
                   print('The perimeter of the sector is %.2f'%(2*r+l))
                   print('The area of the sector is %.2f'%(l*r/2))
                else:
                   if graph=='e':
                      side1,side2,side3=input('Please enter three sides of the triangle:')
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
                                     side1=b
                                  else:
                                     if side2>side3:
                                        c=side3
                                        side3=side2
                                        side2=c
                                     else:
                                         while (side1+side2)<=side3:
                                               side1,side2,side3=input('The number three sides can not build a triangle,please enter again:')      
                   p=(side1+side2+side3)/2
                   print('The perimeter of the graph is %.2f'%(side1+side2+side3))
                   print('The area of the graph is %.2f'%(math.sqrt(p*(p-side1)*(p-side2)*(p-side3))))
    print('\n')
    temp=raw_input('Please enter the name of the graph:')
    graph=str(temp)
     
