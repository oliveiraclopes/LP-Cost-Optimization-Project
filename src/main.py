from pulp import LpProblem, LpMinimize, LpVariable, lpSum, value

problem = LpProblem("Cost_Optimization", LpMinimize)

UC_values = []
print("Insira os valores para cada unidade de custo: ")
for i in range(12):
    uc_value = float(input(f"UC{i+1}: "))
    UC_values.append(uc_value)

RHE_value = float(input("Insira o valor pars Recursos Humanos Econômicos: "))

sT = 0.1
Infra = 0.05

CT = sum(UC_values) + RHE_value
CT_adjusted = CT / (1 - sT - Infra)

funding_embrapii = CT * (1/3)
participation_percentage = (funding_embrapii/CT) * 100

problem += CT_adjusted, "Total_Cost"

# Restrições
problem += (funding_embrapii <= CT_adjusted * (1/3), "Max_Funding_EMBRAPII")
problem += (CT_adjusted - funding_embrapii >= 0, "Remaining_Cost_Non_Negative")

problem.solve()

def format_reais(value):
    return f"R$ {value:,.2f}".replace(",", ".")

print("\nResultados: ")
print("Status: ", problem.status)
print("Custo Total: ", format_reais(CT))
print("Custo Total Ajustado: ", format_reais(value(CT_adjusted)))
print("Financiamento da Embrapii: ", format_reais(funding_embrapii))
print(f"Participação da Embrapii: {participation_percentage:.2f}%")
print("Custo Restante a ser dividido: ", format_reais(CT - funding_embrapii))

for i, val in enumerate(UC_values, start=1):
    print(f"UC{i}: {format_reais(val)}")
print("Recursos Humanos Econômicos: ", format_reais(RHE_value))