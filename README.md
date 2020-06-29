# Busca Ortogonal em Kd-Tree de 2 Dimensões

A princípio quando pensamos em banco de dados, geometria não é o primeiro campo que nos vem a mente. Contudo um grande número de perguntas (queries) sobre os dados, podem ser respondidas de forma geométrica. Para tanto, basta pensarmos nos dados como pontos no espaço. Vamos considerar como exemplo a base de dados de uma empresa que contenha os registros de cada funcionário, tais como nome, endereço, data de aniversário, salário entre outras coisas. Uma pergunta que podemos querer responder seria, quem são os funcionários nascidos entre 1950 e 1955 que ganham entre $3000 e $4000 por mês?

![](images/Kd-Tree%20Orthogonal%20Search.png)

Para respondermos essa pergunta de uma forma geométrica, representamos cada funcionário como um ponto no plano. A primeira coordenada deste ponto seria a data de nascimento, que será representada por um inteiro de forma que seja 10.000 x anos + 100 x meses + dias, e a segunda o salário mensal. A partir disto, podemos considerar que queremos todos os pontos cuja primeira coordenada esteja entre 19.500,000 e 19,559,999, e cuja segunda coordenada enteja entre 3000 e 4000. Em outras palavras, queremos todos os pontos que estão dentro de um retângulo paralelo aos eixos considerados e limitados pela query.
Neste exemplo, o nosso problema pode ser mapeado em 2 dimensões. Contudo, podemos acrescentar quantas restrições quisermos à query, isso apenas aumentaria o número de dimensões com as quais trabalharíamos.
Este tipo de query é chamada de Busca Ortogonal e neste trabalho iremos nos ater a queries com 2 dimensões. Para tanto, utilizaremos uma estrutura de dados chamada Kd-tree para nos auxiliar.

O relatório completo deste projeto se encontra no arquivo **Relatório Projeto Final.pdf**
