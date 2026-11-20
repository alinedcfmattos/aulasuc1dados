#Enunciado:
# Calcule e mostre  número de lâmpadas necessárias para iluminar um cômodo.
#
# Entrada: potência da lâmpada (watts), largura e comprimento do cômodo (metros).
# Considere: 3 watts por metro quadrado a um bocal (soquete) para cada 3m².




# Dicas: 
# - Não existe "meia lâmpada"






#-------------------------------------------------------
import math 

potencia_lampada = float(input("Potência da lâmpada (W): "))
largura = float(input("Largura do cômodo (m): "))
comprimento = float(input("Comprimento do cômodo(m): "))

area = largura * comprimento
potencia_necessaria = area * 3 # 3 W por m²
lampadas = math.ceil(potencia_necessaria/potencia_lampada)
bocais = math.ceil(area/3) # 1 bocal a cada 3m²

print(f"Área do cômodo: {area: .2f} m²")
print(f"Potência necessária: {potencia_necessaria:.0f} W")
print(f"Lâmpadas de {potencia_lampada:.0f} W necessarias: {lampadas}")
print(f"Bocais disponíveis no cômodo: {bocais}")

if lampadas > bocais:
    print("Atenção: faltam bocais! Use lâmpadas mais potentes.")
else: 
    print("Os bocais são suficientes")