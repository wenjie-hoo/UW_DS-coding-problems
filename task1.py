from itertools import product,count

def gen_nums(digit_len):
    num_tuple = list(product((8, 9), repeat=digit_len))
    return [int(''.join(map(str, idx))) for idx in num_tuple]

def is_prime(n):
  if n <= 1: return False
  for i in count(2): 
    if i * i > n: return True
    if n % i == 0: return False
  
def task_1(k=5):
    prime_num = [i for i in gen_nums(k) if is_prime(i)]
    return prime_num
  
print('k=5:',task_1(5))
print('k=10:',task_1(10))
