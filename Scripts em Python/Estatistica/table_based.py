import math
import numpy

def media(lis, c, k, Li):
  i = 0
  med = 0
  li = Li
  lf = li+c
  for _ in range(k):
    med += ((li + lf)/2)*lis[i]
    i += 1
    li = lf
    lf += c
  med /= numpy.sum(lis, 0)
  print("\nMedia: " f'{med:.4f}')
  return med


def variance(lis, li, media, k, c):
  var = 0
  i = 0
  lf = li + c
  for _ in range(k):
    var += ((((li + lf)/2) - media)**2) * lis[i]
    i += 1
    li = round(lf, 2)
    lf = round(lf+c, 2)
  var = var/(numpy.sum(lis, 0)-1)
  print("Variance: " f'{var:.4f}')
  print("Desvio: " f'{math.sqrt(var):.4f}')


def median(lis, c, lic):
  md = 0
  i = 0
  fac1 = 0
  fac2 = 0
  sum = 0
  while fac1 < 0.5:
    sum += lis[i]
    fac1 = (sum / numpy.sum(lis, 0))
    fac2 = (sum / numpy.sum(lis, 0))
    i += 1
  fac1 = fac1 - (lis[i-2]/numpy.sum(lis, 0))
  md = ((c * (0.5 - (fac2 -fac1))) / (fac1)) + ((lic + ((i-1)*c)))
  print("Median: "f'{md:.4f}')

  
def main():
  k = int(input("Input k: "))
  Li = float(input("Input Li: "))
  c = float(input("Input C: "))
  lis = numpy.array([])
  print("Input the Fi's in order separated by \\n's:")
  for _ in range(k):
    temp = int(input())
    lis = numpy.append(lis, temp)
  variance(lis, Li, media(lis, c, k, Li), k, c)
  median(lis, c, Li)

if __name__ == '__main__':
  main()