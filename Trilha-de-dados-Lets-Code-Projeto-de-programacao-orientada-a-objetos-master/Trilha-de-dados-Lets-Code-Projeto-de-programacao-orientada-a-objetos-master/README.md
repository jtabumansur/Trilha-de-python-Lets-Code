# Programacao-orientada-a-objetos-em-Python-
Sistema de empréstimo de bibliotecas, que envolve duas  classes principais (Cliente, Loja)

Observacao- deixei os testes ja prontos no arquivo conjunto de testes 

Brief

Cliente pode: 
• Ver as bicicletas disponíveis na Loja; 

• Alugar bicicletas por hora (R$5/hora);

• Alugar bicicletas por dia (R$25/dia); 

• Alugar bicicletas por semana (R$100/semana) 

• Aluguel para família, uma promoção que 3 ou mais empréstimos (de qualquer  tipo) com 30% de desconto no valor total. 

Loja pode: 
• Calcular a conta quando o cliente decidir devolver a bicicleta; 

• Mostrar o estoque de bicicletas; 

• Receber pedidos de aluguéis por hora, diários ou semanais validando a  possibilidade com o estoque e modo de aluguel existente.


Por questão de simplicidade vamos assumir que: 
• Cada empréstimo segue apenas um modelo de cobrança (hora, dia ou semana); • O cliente pode decidir livremente quantas bicicletas quer alugar; • Os pedidos de aluguéis só podem ser efetuados se houver bicicletas suficientes  disponíveis. 
• Não se preocupem quanto a dinheiro em caixa das Lojas nem dos Clientes.

Ao projetar seus objetos você deve se atentar ao que cada classe será  responsável por fazer, entenda o que cada elemento pode fazer, e em seguida abstraia  o problema para desenhar as classes e seus métodos. Note que nem tudo que um  objeto pode fazer é necessariamente um método desse objeto. 
Utilize a biblioteca datetime para trabalhar com tempo no seu programa. 

Você provavelmente vai querer testar o funcionamento e relação dessas classes,  para isso use um terceiro arquivo que usa pelo menos três instâncias de Cliente e duas  de Loja e testa a integração e funcionamento das duas classes. Para facilitar o fluxo  das chamadas use prints em cada método que funcionem como logs, um bom log  consiste em informar de onde ele vem (classe que printou o log), o que ele está  fazendo (qual método), com quais informações (os parâmetros recebidos) e o momento  que ocorreu. 
Faça validações, e gere erros caso alguma validação falhe (raise), note que é  comum logarmos (neste caso, com o print) quando algum erro ocorreu em nosso  sistema. 


