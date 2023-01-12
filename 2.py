number_a=1
number_b=2
my_sum=0

while number_a < 4000000:
    if number_a%2 == 0:
        my_sum += number_a
    if number_b%2 == 0:
        my_sum += number_b
    number_a += number_b
    number_b += number_a
print(my_sum)

    