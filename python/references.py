# blobs created as copy of reference to peeps object
peeps = ['Snoopy','calvin','hobbes']
blobs = peeps
blobs[0] = 'blob'
print(peeps)
print(blobs)

# blobs created as reference to copy of peeps object
peeps = ['Snoopy','calvin','hobbes']
blobs = peeps[0:]   # is not whole peeps object, so copy is made
blobs[0] = 'blob'
print(peeps)
print(blobs)
