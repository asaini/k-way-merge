import heapq


def kmerge(iterables, keyFcn=None):
    '''Merge multiple SORTED inputs into a single sorted output.

    INPUT : @iterables : A list of lists, each of which is a sorted stream
            @keyFcn    : A key function which allows us to operate upon the values in itertables to get values. (Default : None)
	    		 Eg. In a file which stores numbers as string, the values need to be changed to integers before comparison.
			 This is done by using the int(x) function.
    
    Iterators iterate over the input files/iterables reading from the first elements and put them into a
    in memory min-heap. Since we're using iterators we don't have to read the whole file into memory

    OUTPUT: Returns a generator, which does not pull the data into memory all at once, and assumes that each of
    the input streams is already sorted (smallest to largest).

    '''
    _heappop, _heapreplace, _StopIteration = heapq.heappop, heapq.heapreplace, StopIteration
    _iter = iter

    h = []
    h_append = h.append

    for itnum, it in enumerate(map(iter, iterables)):
        try:
            next = it.next
	    if keyFcn is not None:
		h_append([keyFcn(next()),itnum,next])
	    else:
            	h_append([next(), itnum, next])

        except _StopIteration:
            pass
    #print h
    heapq.heapify(h)

    while 1:
        try:
            while 1:
                v, itnum, next = s = h[0]   # raises IndexError when h is empty
                yield v
		if keyFcn is not None:
			s[0] = keyFcn(next())
		else:
                	s[0] = next()       # raises StopIteration when exhausted
                _heapreplace(h, s)          # restore heap condition
        except _StopIteration:
            _heappop(h)                     # remove empty iterator
        except IndexError:
            return


if __name__=="__main__":
	
	#Merge in memory lists of numbers. Lists may be of variable length
	x =kmerge([
			[1,3,5,7], 
			[0,2,4,8], 
			[5,10,15,20], 
			[], 
			[25]
		  ])

	for i in x:
		print i

	print '\n\n'

	#Merge from two files each of which is a sorted stream of numbers
	f1 = open('List1')
	f2 = open('List2')

	x = kmerge([f1,f2],int)
	
	for i in x:
		print i
	
	#Try to merge two empty lists
	x = kmerge([[],[]])
	for i in x:
		print i
	print '\n\n'

	#Merge from 2 files which contains a list of strings sorted lexicographically
	f1 = open('File1')
	f2 = open('File2')

	x = kmerge([f1,f2],str.rstrip)
	
	for i in x:
		print i
	
