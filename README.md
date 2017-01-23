## K-Way Merge

Given k sorted streams (k could be large), this operator accepts a list of the k streams and output a stream 'O' and outputs a single, fully sorted stream to 'O'

It uses k Python Iterators to iterate over the input streams so all of the data is not loaded into memory, each element is lazily loaded which uses only a constant amount of memory. The output is a Generator object which only yields 1 element at a time. Again this is done lazily as and when output is required from the output stream.

The code is a slight reorganization of Python's heapq. 


