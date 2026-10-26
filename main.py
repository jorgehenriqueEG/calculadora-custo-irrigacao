area = 50
solo = 'arenoso'
custo_m2 = 2.5

fator = 1.0
if solo == 'arenoso':
    fator = 0.75
elif solo == 'argiloso':
    fator = 1.0
else:
    fator = 1.2

custo_total = area * custo_m2 * fator
print(f'Custo total: R$ {custo_total:.2f}')