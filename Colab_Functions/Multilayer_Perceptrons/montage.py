def montage(x, return_grid=False):
  num = int(np.sqrt(x.shape[0]))
  m = int(np.ceil(np.sqrt(x.shape[1])))
  n = m
  grid = np.zeros([num*m, num*n])
  
  for i in range(num):
    for j in range(num):
      grid[i*m:i*m+m, j*n:j*n+n] = bytescale(x[i*num+j, ...].reshape([28, 28]))
      
  if return_grid:
    return grid
      
  fig = plt.figure(figsize=(15, 15))
  a1 = fig.add_subplot(111)
  a1.imshow(grid, cmap='gray')
  a1.grid(False)
  plt.show()
