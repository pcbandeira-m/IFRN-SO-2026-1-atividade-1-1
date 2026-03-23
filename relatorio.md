# IFRN - Atividade Avaliativa da disciplina de Sistemas Operacionais - Prof: Leonardo Minora

## Introdução
Esta atividade tem como objetivo ensinar a criar e executar containers `Docker` com `Python` para a disciplina de `Sistemas Operacionais`.

## Relato das atividades
Toda a atividade foi dividida em passos, como a seguir:
- <strong>Preparação do projeto</strong>, onde criei um fork do repositório original do professor Minora e, então, o clonei para a minha máquina. Depois, criei uma pasta `app` e, nela, adicionei o arquivo `requirements.txt`.
- <strong>Criação da imagem Docker e execução do container</strong>, onde, primeiramente, criei um arquivo `Dockerfile.dev` na pasta app e depois construí a `imagem` de desenvolvimento e executei o `container`.
- <strong>Criação e configuração da aplicação Django</strong>, onde foi possível criar o `projeto Django` e sua aplicação dentro do container. Então, configurei o banco de dados `SQLite3`, adicionei a aplicação ao arquivo myproject/settings.py e o editei no ALLOWED_HOSTS para aceitar todas as conexões. Depois, executei as migrações do banco de dados, criei o `superusário admin`, criei uma view simples no webapp e configurei as URLs da aplicação e as do projeto.
- Por último, tornei a <strong>aplicação Django acessível para a execução</strong>:
<br>
<br>
    ```txt
    Página inicial: http://localhost:8000
    Admin: http://localhost:8000/admin (use username: admin, password: 321)
    ```


## Considerações finais

Considero esta uma atividade essencial para os primeiros contatos com a disciplina. Alguns conceitos ainda estão sendo introduzidos e minhas maiores dificuldades foram alguns momentos de travamento no terminal, mas o auxílio do professor durante o exercício me ajudou a entender o que estava acontecendo e consegui concluir tudo o que estava sendo proposto. Entretanto, precisei fechar o terminal algumas vezes para fazer funcionar o que estava dando problema, então a maioria das saídas não ficaram salvas para registro neste relatório.