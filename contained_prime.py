from itertools import product,count

def gen_nums(digit_len):
    num_tuple = list(product((8, 9), repeat=digit_len))
    nums = [int(''.join(map(str, idx))) for idx in num_tuple]
    return nums

def is_prime(n):
  if n <= 1: 
    return False
  for i in count(2): 
    if i * i > n: 
      return True
    if n % i == 0: 
      return False
  
def task_1(k):
    nums_list = gen_nums(k)
    prime_num = []
    for i in nums_list:
        res = is_prime(i)
        if res:
            prime_num.append(i)
    return prime_num

print(task_1(5))  