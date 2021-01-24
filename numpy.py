import numpy as np
a = np.random.normal(size=(20, 20))
b = np.random.randint(100,size=(20, 1))
def theta(X,y):
  xtxinv=np.linalg.inv(np.dot(X.T,X))
  xty=np.dot(X.T,y)
  return np.dot(xtxinv,xty)
theta(a,b)