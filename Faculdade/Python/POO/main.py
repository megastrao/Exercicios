import Salario
import Empregado

salario = Salario(10000, 700)
emp = Empregado('Musashi', 46, salario)
print(emp.salario_total())
