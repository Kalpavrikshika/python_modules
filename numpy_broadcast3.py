import numpy as np 
x = np.array([[1], [2], [3]]) 
y = np.array([4, 5, 6])  
   
# tobroadcast x against y 
b = np.broadcast(x,y)  
# it has an iterator property, a tuple of iterators along self's "components." 

print ('Broadcast x against y:' )
r,c = b.iters 
print (r.next(), c.next())
print (r.next(), c.next())
print ('\n')  
# shape attribute returns the shape of broadcast object 

print ('The shape of the broadcast object:' )
print (b.shape )
print ('\n')
# to add x and y manually using broadcast 
b = np.broadcast(x,y) 
c = np.empty(b.shape) 

print ('Add x and y manually using broadcast:') 
print (c.shape )
print ('\n' ) 
c.flat = [u + v for (u,v) in b] 

print ('After applying the flat function:') 
print (c )
print ('\n'  )
# same result obtained by NumPy's built-in broadcasting support 

print ('The summation of x and y:') 
print (x + y)