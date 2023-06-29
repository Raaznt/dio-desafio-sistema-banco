# DIO - Desafio de Código

## Problema

" Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar extrato. Além disso, para aversão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com o usuário)."

## Descrição do problema

### **Separação em funções**

"Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra de passagem de argumentos. O retorno e a forma como serão chamadas podem ser definidos da forma que achar melhor."

### **Operação de saque**

"A função saque deve receber os argumentos apenas por nome (_keyword only_). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato."

### **Operação depósito**

"A função depósito deve receber os argumentos apenas por posição (_positional only_). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato."

### **Operação extrato**

"A função extrato deve receber os argumentos por posição e nome (_positional only_ e _keyword only_). Argumentos posicionais: saldo. Argumentos nomeados: extrato."

### **Novas funções**

"Precisamos criar duas novas funções: criar usuário e criar conta corrente. Fique a vontade para adicionar mais funções. Exemplo: listar contas."

### **Criar usuário (cliente)**

"O programa deve armazenar os usuários em uma lista. Um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro,nro-bairro-cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF."

### **Criar conta corrente**

"O programa deve armazenar contas em uma lista. Uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário."
