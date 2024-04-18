first_product = input()
second_product = input()

code, count, price = first_product.split(' ')
prod1_total = int(count) * float(price)

code, count, price = second_product.split(' ')
prod2_total = int(count) * float(price)
res = prod1_total + prod2_total
print(f"VALOR A PAGAR: R$ {res:.2f}")