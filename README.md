# [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Ubuntu&size=20&color=17CE1D&center=false&lines=BLOG+ROOM)](https://git.io/typing-svg)
O objetivo deste projeto é simular um sistema  de blog utilizando sockets, em que uma pessoa pode fazer uma postagem enquanto outras pessoas podem visualizar e curtir.

# Alunos
Filipe Ferreira Figueredo Soriano Pinto
Ricardo Vinicius de Almeida Fernandes
Vinicius Rafael MArques de Carvalho

# Instruções de uso
O primeiro passo para executar a aplicação é iniciar a conexão do servidor, para isso é necessário executar o arquivo y.py em um prompt de comando adicionar a flag -s para indicar que uma conexão de servidor deve ser iniciada, em seguida adicionar o ip em que o servidor vai rodar e a porta.
Exemplo: python3 y.py -s localhost 1234.

O passo para criar a conexão do cliente é semelhante, é necessário executar o arquivo y.py, adicionar a flag -c, colocar o ip do servidor e a porta.
Exemplo: python3 y.py -c localhost 1234.

Após iniciar a conexão do cliente será exibida uma interface com as funcionalidades disponíveis, como criar post, visualizar post e encerrar a conexão.

A partir do servidor é possível visualizar as solicitações dos clientes em um formato JSON.
