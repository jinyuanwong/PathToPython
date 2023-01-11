
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm


def ReadTextFromUnrealEngine(textname):
    if textname == None:
        textname = 'test.txt'
    with open(textname) as f:
        lines = f.readlines()
    len_lines = len(lines)
    x,y,z = [],[],[]
    for i in range(len_lines):

        # line example:  X=00.000 Y=00.000 Z=0.0000
        data = lines[i] 

        # Find the value location
        location_y = data.find('Y=')
        location_z = data.find('Z=')
        value_x = float(data[2:location_y])
        value_y = float(data[location_y+2:location_z])
        value_z = float(data[location_z+2:])

        # Append the value to the x,y,z
        x.append(value_x)
        y.append(value_y)
        z.append(value_z)
    return x,y,z


if __name__ == '__main__':

    # Read the x,y,z speed
    X,Y,Z = ReadTextFromUnrealEngine(None)

    print(f'Total len: {len(X)}')


    # Select Location of begin and end of breath in UE
    begin_loc,end_loc = 17,380
    # print(X.index(-4.325)) #380
    # print(X.index(-0.194)) #17
    X = X[begin_loc:end_loc]
    Y = Y[begin_loc:end_loc]
    Z = Z[begin_loc:end_loc]


    # Average the data with 6 datapoint
    mean_x = []
    print(len(X)-4)
    for i in range(3,len(X)-4):
        mean_x.append(sum(X[i-3:i+3]) / 6)


    #Algorithm to recognise the breath     
    
    breathe_up = 0
    breathe_down = 0 
    threhold = 0.15        
    i = 10
    
    # collection of the all chosen points
    up_i = []
    while i < len(mean_x)-10:
        if mean_x[i] - mean_x[i-10]> threhold:
            print(i)
            up_i.append(i)
            i+=10
            breathe_up += 1
        i+=1
    print(f'breathe up: {breathe_up}')

    
    # Plot the speed
    plt.figure(1)
    plt.plot(mean_x,'b')
    for i in up_i:
        plt.scatter(i,mean_x[i])
    # plt.plot(Y,'r')
    # plt.plot(Z,'y')
    plt.xlabel('Time')  
    plt.xlabel('Speed')
    plt.show()




    



