def pascal(n, k):
    if k==0 or n==k:
        r=1
    else:
        r=pascal(n-1,k)+pascal(n-1,k-1)
    return r

if __name__=="__main__":
    print(pascal(4,2))
    print(pascal(5,2))
