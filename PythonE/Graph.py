import math
temp=raw_input('Please enter the name of the graph:')
graph=str(temp)
if graph=='rectangle':
    l=input('Please enter the length of the graph:')
    w=input('Please enter the width of the graph:')
    print('The perimeter of the graph is %.2f'%(2*l+2*w))
    print('The area of the graph is %.2f'%(l*w))
else:
    if graph=='square':
        l=input('Please enter the length of the graph:')
        print('The perimeter of the graph is %.2f'%(4*l))
        print('The area of the graph is %.2f'%(l*l))
    else:
        if graph=='circular':
            r=input('Please enter the radius of the graph:')
            print('The perimeter of the graph is %.2f'%(2*math.pi*r))
            print('The area of the graph is %.2f'%(math.pi*r*r) )
        else:
            if graph=='sector':
                r=input('Please enter the radius of the graph:')
                n=input('Please enter the angle of the graph:')
                l=n*math.pi*r/180
                print('The perimeter of the graph is %.2f'%(2*r+l))
                print('The area of the graph is %.2f'%(l*r/2))
            else:
                if graph=='triangle':
                    side1=input('Please enter first side of the graph:')
                    side2=input('Please enter second side of the graph:')
                    side3=input('Please enter third side of the graph:')
                    p=(side1+side2+side3)/2
                    print('The perimeter of the graph is %.2f'%(side1+side2+side3))
                    print('The area of the graph is %.2f'%(math.sqrt(p*(p-side1)*(p-side2)*(p-side3))))
