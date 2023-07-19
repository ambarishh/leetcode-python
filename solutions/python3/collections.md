# Common Python Collections
<!-- TOC -->
* [Common Python Collections](#common-python-collections)
    * [Deque](#deque)
    * [Default Dictionary](#default-dictionary)
    * [String](#string)
    * [Matrix](#matrix)
    * [Set](#set)
<!-- TOC -->

### Deque
* append() : Stack 
* appendLeft() : Queue
* pop()
* popLeft()
* insert(idx, val)

### Sorted Containers
##### SortedList
##### SortedSet
##### SortedDict
* add()
* remove()

### Default Dictionary
* defaultdict(int) : default values of key is 0
* defaultdict(list) : default values of key is list

### String
* isalnum()
* lower()

### Matrix
Define M*N matrix as `[[0]*N for _ in range(M)]`

### Set
* union() : `x1 | x2`
* intersection() : `x1 & x2`
* difference() : `x1-x2 / x1.difference(x2)` -> elem in x1 but not in x2
* symmetric_difference() :` x1 ^ x2` / all elems which are not in both x1 & x2