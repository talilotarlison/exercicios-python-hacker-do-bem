-- Para usar o SQLite com JavaScript, você tem algumas opções interessantes:

-- https://github.com/sql-js/sql.js/
-- https://lovasoa.github.io/sql.js/documentation/

-- SQL.js: Esta biblioteca permite executar o SQLite diretamente no navegador usando JavaScript. Ela é baseada no projeto sql.js e inclui várias melhorias. Aqui está um exemplo de como usá-la:

-- <script src="js/sql.js"></script>

-- <script>
--     // Crie o banco de dados
--     var db = new SQL.Database();

--     // Execute uma consulta sem ler os resultados
--     db.run("CREATE TABLE test (col1, col2);");

--     // Insira duas linhas: (1,111) e (2,222)
--     db.run("INSERT INTO test VALUES (?,?), (?,?)", [1, 111, 2, 222]);

--     // Prepare uma instrução
--     var stmt = db.prepare("SELECT * FROM test WHERE col1 BETWEEN $start AND $end");
--     stmt.getAsObject({ $start: 1, $end: 1 }); // { col1: 1, col2: 111 }

--     // Associe novos valores
--     stmt.bind({ $start: 1, $end: 2 });
--     while (stmt.step()) {
--         var row = stmt.getAsObject();
--         // Faça algo com a linha de resultado
--     }
-- </script>

-- Você pode encontrar mais informações e documentação detalhada aqui1.
-- IndexedDB: Se você está interessado apenas no aspecto do banco de dados, o IndexedDB é uma alternativa. Ele é uma API de armazenamento de dados no navegador que permite que você armazene e recupere dados de forma eficiente.
-- Lembre-se de que, para usar o SQL.js, você precisará de um ambiente JavaScript, como o Node.js, para executar o código. Espero que isso ajude! 


-- O SQL.js é uma biblioteca que permite executar o SQLite diretamente no navegador usando JavaScript. Vamos entender como ele lida com o armazenamento de dados:

-- Armazenamento em Disco:
-- O SQL.js não gera um arquivo em disco diretamente. Ele opera na memória do navegador. Quando você cria um banco de dados usando o SQL.js, ele é criado na memória do navegador e não em um arquivo físico no disco.
-- Isso significa que os dados não são persistentes entre sessões ou recargas da página. Quando a página é atualizada ou fechada, os dados do banco de dados são perdidos.
-- Armazenamento no Navegador:
-- O SQL.js armazena os dados na memória do navegador, mas não no armazenamento local do dispositivo (como o sistema de arquivos).
-- Se você deseja armazenar dados de forma persistente no navegador, considere usar outras tecnologias, como o IndexedDB.
-- O IndexedDB é uma API de armazenamento de dados no navegador que permite que você crie bancos de dados persistentes e recupere dados mesmo após a atualização ou fechamento da página.
-- Portanto, se você precisa de armazenamento persistente em disco, o SQL.js não é a melhor opção. Nesse caso, explore outras alternativas, como o IndexedDB ou considere usar um servidor para armazenar dados de forma mais duradoura. 