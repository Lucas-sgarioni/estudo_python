#Referência: https://www.tutorialspoint.com/pytest/pytest_quick_guide.htm

import pytest

data = [(5,5, 25)]  #Entrada = 1, que vezes 5 deve ter Saída=5
  #Entrada = 6, que vezes 5 deve ter Saída=30 (Erro Proposital a ser observado)
@pytest.mark.parametrize("primeiro, segundo, saida", data)
def test_multiplication_by_5(primeiro, segundo, saida):
   assert primeiro * segundo == saida
   print('valor de saída =', saida)