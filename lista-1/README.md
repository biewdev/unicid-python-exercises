## Lista 1

##### ACERTOS

<p>Escreva um programa que corrija um teste de múltiplas escolhas, mostrando a quantidade de
acertos, contendo três questões, cada questão possui 5 alternativas do tipo a, b, c, d e e. A
resposta correta da primeira questão é “b”; da segunda, “a”; e da terceira, “d”. O programa
conta um ponto a cada resposta correta. Considere a possibilidade do programa aceitar
respostas com letra maiúsculas e minúsculas em todas as questões. Dê o nome do seu
programa de acertos.py.</p>
<ul>
    <li>Código: <a href="./acertos.py">acertos.py</a></li>
    <li>Saída dando os valores 'B', 'A' e 'D':</li>
</ul>

```
> Resposta da primeira questão: B
> Resposta da segunda questão: A
> Resposta da terceira questão: D
Total de pontos: 3
```

<ul>
    <li>Saída dando os valores 'A', 'A' e 'D':</li>
</ul>

```
> Resposta da primeira questão: A
> Resposta da segunda questão: A
> Resposta da terceira questão: D
Total de pontos: 2
```

<ul>
    <li>Saída dando os valores 'A', 'B' e 'D':</li>
</ul>

```
> Resposta da primeira questão: A
> Resposta da segunda questão: B
> Resposta da terceira questão: D
Total de pontos: 1
```

<ul>
    <li>Saída dando os valores 'A', 'B' e 'A':</li>
</ul>

```
> Resposta da primeira questão: A
> Resposta da segunda questão: B
> Resposta da terceira questão: A
Total de pontos: 0
```
<br>

##### EMPRESTIMO
<p>Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O
programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da
prestação como sendo o valor da casa a comprar dividido pelo numero de meses a pagar. Dê o
nome do seu programa de emprestimo.py.</p>
<ul>
    <li>Código: <a href="./emprestimo.py">emprestimo.py</a></li>
    <li>Saída dando os valores '70000', '5000' e '5':</li>
</ul>

```
> Qual o valor da casa? 70000
> Valor da casa: 70000.0
> Qual o valor do salário? 1500
Salario: 1500.0
Qual a quantidade de anos para pagar? 5
Anos a pagar: 5
Empréstimo Negado
```

<ul>
    <li>Saída dando os valores '70000', '1500' e '5':</li>
</ul>
<br>

##### ORDEM DE GRANDEZA
<p>Fazer um programa que leia um número e exiba a ordem de grandeza seguindo a tabela abaixo.
Dê o nome do seu programa de ordem_grandeza.py.</p>
<table>
    <tr>
        <td>X >= 0 e X < 100</td>
        <td>exibir</td>
        <td>“X entre 0 e 100”</td>
    </tr>
    <tr>
        <td>X >= 100 e X < 1000</td>
        <td>exibir</td>
        <td>“X entre 100 e 1000”</td>
    </tr>
    <tr>
        <td>X >= 1000</td>
        <td>exibir</td>
        <td>“X maior ou igual a 1000”</td>
    </tr>
    <tr>
        <td>X < 0</td>
        <td>exibir</td>
        <td>“X menor que zero”</td>
    </tr>
</table>
<ul>
    <li>Código: <a href="./ordem_grandeza.py">ordem_grandeza.py</a></li>
    <li>Saída dando o valor '50':</li>
</ul>

```
> Digite o valor do numero: 50
50 entre 0 e 100
```

<ul>
    <li>Saída dando o valor: '200':</li>
</ul>

```
> Digite o valor do numero: 200
200 entre 100 e 1000
```

<ul>
    <li>Saída dando o valor: '5000':</li>
</ul>

```
> Digite o valor do numero: 5000
5000 maior ou igual a 1000
```

<ul>
    <li>Saída dando o valor: '-1':</li>
</ul>

```
> Digite o valor do numero: -1
-1 menor que zero
```
<br>

##### Palíndromo
<p>Escreva um programa que verifique se um numero é palíndromo. Um número palíndromo se
continua o mesmo caso seus dígitos sejam invertidos. Exemplo: 454, 10501. Dê o nome do seu
programa de palindromo.py.</p>
<ul>
    <li>Código: <a href="./palindromo.py">palindromo.py</a></li>
    <li>Saída dando o valor '454':</li>
</ul>

```
> Digite o número: 454
É palíndromo
```
<ul>
    <li>Saída dando o valor '155:'</li>
</ul>

```
> Digite o número: 155
Não é palíndromo
```
<br>

##### PASSAGEIRO
<p>Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e R$ 0,45
para viagens mais longas. Dê o nome do seu programa de passageiro.py.</p>
<ul>
    <li>Código: <a href="./passageiro.py">passageiro.py</a></li>
    <li>Saída dando o valor '100':</li>
</ul>

```
> Qual a distância da viagem em km/h? 100
O valor da viagem é de: 50.0
```
<ul>
    <li>Saída dando o valor '300':</li>
</ul>

```
> Qual a distância da viagem em km/h? 300
O valor da viagem é de: 135.0
```
<br>

##### TROCO
<p>Programa troco. Dê o nome do seu programa de troco.py</p>
<ol type="a">
    <li>Escreva um programa que leia um valor e que imprima a quantidade de cédulas
    necessárias para pagar esse mesmo valor. Para simplificar utilize números inteiros e com
    cédulas de R$50, R$20, R$10, R$4 e R$1. Após concluído, faça testes com os seguintes
    valores: 50, 745, 384, 2, 7 e 1.</li>
    <li>Modifique o item a para trabalhar com nota de R$ 100,00. O que acontece se for digitado
    0 (zero) no valor a pagar? Ajuste seu programa.</li>
    <li>Modifique o programa do item a para aceitar valores decimais, ou seja, também contar
    moedas de R$0.01, R$0.02, R$0.05, R$0.10, e R$0.50.</li>
    <li>No item d, o que acontece se digitarmos 0.001? Caso ele não funcione, altere-o de forma
    a corrigir esse problema.</li>
    <li>Reescreva de forma a continuar executando até que o valor digitado seja 0. Utilize
    repetições aninhadas.</li>
    <li>No final você deverá ter apenas um único programa: troco.py.</li>
</ol>
<ul>
    <li>Código: <a href="./troco.py">troco.py</a></li>
    <li>Saída dando o valor '50':</li>
</ul>

```
> Digite o valor: 50
1 nota(s) de R$ 50
```
<ul>
    <li>Saída dando o valor '745':</li>
</ul>

```
> Digite o valor: 745
7 nota(s) de R$ 100
2 nota(s) de R$ 20
1 nota(s) de R$ 4
1 nota(s) de R$ 1
```
<ul>
    <li>Saída dando o valor '384':</li>
</ul>

```
> Digite o valor: 384
3 nota(s) de R$ 100
1 nota(s) de R$ 50
1 nota(s) de R$ 20
1 nota(s) de R$ 10
1 nota(s) de R$ 4
```
<ul>
    <li>Saída dando o valor '2':</li>
</ul>

```
> Digite o valor: 2
2 nota(s) de R$ 1
```
<ul>
    <li>Saída dando o valor '7':</li>
</ul>

```
> Digite o valor: 7
1 nota(s) de R$ 4
3 nota(s) de R$ 1
```
<ul>
    <li>Saída dando o valor '1':</li>
</ul>

```
> Digite o valor: 1
1 nota(s) de R$ 1
```
<ul>
    <li>Saída dando o valor '0.01':</li>
</ul>

```
> Digite o valor: 0.01
1 moeda(s) de 0.01 centavo(s)
```
<ul>
    <li>Saída dando o valor '0.05':</li>
</ul>

```
> Digite o valor: 0.05
1 moeda(s) de 0.05 centavo(s)
```
<ul>
    <li>Saída dando o valor '0.10':</li>
</ul>

```
> Digite o valor: 0.10
1 moeda(s) de 0.1 centavo(s)
```
<ul>
    <li>Saída dando o valor '0.50':</li>
</ul>

```
> Digite o valor: 0.50
1 moeda(s) de 0.5 centavo(s)
```
<ul>
    <li>Saída dando o valor '0':</li>
</ul>

```
> Digite o valor: 0
Não aceitamos valores abaixo de 0.01 centavo(s)
```
