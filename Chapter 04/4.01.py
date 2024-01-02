import random

rand_int = random.randint(0, 10)
print(rand_int)

rand_float = random.random()
print(rand_float)

# membuat random float dengan interval 0.0000 s.d 4.9999
rand_float2 = random.random() * 5
rand_float3 = random.uniform(0, 5)
print(rand_float2)
print(rand_float3)
