'''
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
'''


def flipAndInvertImage(A):
    temp=[]
    for a in A:
        t=[]
        for i in a:
            if i==1:
                i=0
            else:
                i=1
            t.append(i)
        t.reverse()
        temp.append(t)
    return temp

print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))