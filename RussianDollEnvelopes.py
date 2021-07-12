'''In this question we just have to use longest increasing subsequence on the heights og the enevelopes
the LIS we use is not by dp but by simple binary search'''



def russianDoll(envelopes):
    if not envelopes:
        return 0
    
    envelopes.sort(key=lambda x:(x[0],-x[1]))

    result = [0]*len(envelopes)
    size = 0

    for envelope in envelopes:
        i,j=0,size
        while i!=j:
            mid = (i+j)//2

            if result[i]<envelope[1]:
                i = mid+1
            else:
                j =mid

        result[i] = envelope[1]
        size = max(size,i+1)
    
    return size




#one more approach much easier to understand

def russianDoll2(envelopes):
    if not envelopes:
        return 0
    
    envelopes.sort(key=lambda x:(x[0],-x[1]))

    result = [0]*len(envelopes)
    size = 0

    for i in range(len(envelopes)):
        for j in range(i):
            if envelopes[i][1]>envelopes[j][1]:
                if result[i] == result[j]:
                    result[i] =  result[j] +1

envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(russianDoll(envelopes))