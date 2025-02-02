#12
def histogram(lst):
  for num in lst:
    print('*' * num)

lst = list(map(int, input().split()))

histogram(lst)