----------------------------------------------------
-- Atividade II - Banco de Dados II - UTFPR
-- Desenvolvido por Luiz Ricardo Brumati De Lima
----------------------------------------------------

CREATE TABLE Aluno(
    Nome VARCHAR(50) NOT NULL,
    RA DECIMAL(8) NOT NULL,
    DataNasc DATE NOT NULL,
    Idade DECIMAL(3),
    NomeMae VARCHAR(50) NOT NULL,
    Cidade VARCHAR(30),
    Estado CHAR(2),
    Curso VARCHAR(50),
    periodo integer
);

CREATE TABLE Discip(
    Sigla CHAR(7) NOT NULL,
    Nome VARCHAR(25) NOT NULL,
    SiglaPreReq CHAR(7),
    NNCred DECIMAL(2) NOT NULL,
    Monitor DECIMAL(8),
    Depto CHAR(8)
);

CREATE TABLE Matricula(
    RA DECIMAL(8) NOT NULL,
    Sigla CHAR(7) NOT NULL,
    Ano CHAR(4) NOT NULL,
    Semestre CHAR(1) NOT NULL,
    CodTurma DECIMAL(4) NOT NULL,
    NotaP1 NUMERIC(3,1),
    NotaP2 NUMERIC(3,1),
    NotaTrab NUMERIC(3,1),
    NotaFIM NUMERIC(3,1),
    Frequencia DECIMAL(3)
);

--drop table aluno, discip, matricula cascade;

-- Exercício 1 --------------------------------------------------------
-----------------------------------------------------------------------

-- Constraints:

-- Define a PK como o RA do aluno e a torna exclusiva
alter table aluno add constraint ra_aluno_pk primary key (ra);

-- Define a PK como a sigla do Disciplina e a torna exclusiva
alter table discip add constraint sigla_discip_pk primary key (sigla);

-- Define a PK como o RA do aluno e a sigla do Disciplina, de acordo com
--o ano e semestre de matricula
alter table matricula add constraint ra_sigla_ano_semestre_matricula_pk
primary key (ra, sigla, ano, semestre);

-- Relaciona o monitor da disciplina com RA aluno
alter table discip add constraint monitor_discip_fk
foreign key (monitor) references aluno (ra);

-- Relaciona o ra do aluno com o ra do aluno matriculado
alter table matricula add constraint aluno_matricula_fk
foreign key (ra) references aluno (ra);

-- Relaciona o a sigla da matricula com a sigla da disciplina
alter table matricula add constraint matricula_discip_fk
foreign key (sigla) references discip (sigla);


----------------------------------------------------------------------------------------------------
-- Os dados foram gerados com a utilização do arquivo 'gerar_dados.py', escrito em python.
-- Para popular as tabelas, basta executar o script "tables_population.sql" uma única vez.

analyze aluno;
analyze discip;
analyze matricula;

-- Exercício 2 --------------------------------------------------------
-----------------------------------------------------------------------

CREATE UNIQUE INDEX IdxAlunoNNI ON Aluno (Nome, NomeMae, Idade);
-- O índice só será criado caso não exista nenhuma tupla com os mesmos valores para os campo nome, nomeMae e Idade.


-- Exemplo de consulta que utiza o índice criado:
explain analyze
select nome, nomemae from aluno where nome = 'Luiz' and nomemae = 'Marcieli';

-- Exemplo de consulta que não utiliza o índice criado:
explain analyze
select nome, nomemae from aluno where nomemae = 'Marcieli';

/* Embora utilize um dos campos indexados (nomemae), a busca ainda é realizada de forma sequencial, visto que
o campo 'NomeMae' foi indexado DEPOIS do campo 'Nome' e, portanto, possui menor prioridade. Isto significa que,
para o índice ser utilizado, a busca deve conter o primeiro campo (Com maior prioridade), para depois realizar
a busca nos campos seguintes. */

drop index IdxAlunoNNI;

-- Exercício 3 --------------------------------------------------------
-----------------------------------------------------------------------

create extension btree_gin;
create unique index IdxAlunoRaNome ON Aluno (RA, nome);
create index IdxSiglaBitmap on Matricula using gin (Sigla);


-- a) Sequential Scan ----------------------------------------------------
explain analyze
select ra, nome, cidade from aluno where cidade = 'Curitiba';

-- b) Bitmap Index Scan --------------------------------------------------
explain analyze
select sigla from matricula where sigla = 'ZCRAEPG';

-- c) Index Scan ---------------------------------------------------------
explain analyze
select ra, cidade from aluno where ra = 72435763; -- A busca utiliza índices, mas precisa recuperar dados na tabela de origem

-- d) Index-Only Scan ----------------------------------------------------
explain analyze
select ra, nome from aluno where ra = 72435763 and nome = 'Camila'; -- A busca utiliza índices e recupera os dados de lá, sem buscar na tabela de origem.

-- e) Multi-Index Scan ---------------------------------------------------
explain analyze
select matricula.sigla, aluno.ra from matricula, aluno
where matricula.sigla = 'ZCRAEPG' and aluno.ra = 72435763; -- A busca é realizada utilizando dois índices ao mesmo tempo


drop index IdxAlunoRaNome;
drop index IdxSiglaBitmap;

-- Exercício 4 --------------------------------------------------------
-----------------------------------------------------------------------

-- Exemplo 1:
create index IdxMatriculaSiglaFK on Matricula (sigla);

explain analyze
select nome, notaFIM
from matricula natural join discip
where sigla = 'ZYZZCDQ';

drop index IdxMatriculaSiglaFK;

-- Exemplo 2:

create index IdxDiscipMonitorFK on Discip (monitor);

explain analyze
select nome, sigla, periodo
from discip natural join aluno
where monitor = 46953510;

drop index IdxDiscipMonitorFK;


-- Exercício 5 --------------------------------------------------------
-----------------------------------------------------------------------
create index IdxAlunoPeriodo on Aluno using gin (periodo);

explain analyze
select periodo from aluno
where periodo = 9;

drop index IdxAlunoPeriodo;

-- Exercício 6 --------------------------------------------------------
-----------------------------------------------------------------------
create index IdxAlunoNomeIdade ON Aluno (nome, idade);

cluster aluno using IdxAlunoNomeIdade;
-- Ao criar um cluster com base no índice, a tabela é fisicamente reordenada!
analyze aluno;

explain analyze
select nome, idade from aluno
where nome = 'Luiz';


drop index IdxAlunoNomeIdade cascade;

-- Exercício 7 --------------------------------------------------------
-----------------------------------------------------------------------
alter table aluno
add column informacoesExtras jsonb;

-- Geração de valores aleatórios para o campo JSON:
---------------------------------------------------
do $$
declare 
  table_row aluno%rowtype;
  j numeric;
  times varchar[] = '{"Chapecoense","Palmeiras","São Paulo","Internacional", "Flamengo",
                    "Santos","Atlético-MG","Fluminense", "Ceará", "Corinthians", "Botafogo"}';
begin
  for table_row in select * from aluno
  loop
    j = round(random() * 10)+1;
    update aluno set informacoesExtras = 
    (('{
        "telefone" : ' || round(random()*100000000)||',
        "time" : "'|| times[j] ||'"
        }')::json)
    where ra = table_row.ra;
  end loop;
end $$
language plpgsql;
---------------------------------------------------


-- Exemplo 1 de utilização de índices com JSON:
create index idxAlunoJSONTime on aluno using BTREE ((informacoesExtras->>'time'));

explain analyze
select nome, informacoesExtras from aluno
where informacoesExtras->>'time' = 'Internacional';

drop index idxAlunoJSONTime;

-- Exemplo 2 de utilização de índices com JSON:
create index idxJSON on aluno using gin ((informacoesExtras->>'telefone'));

explain analyze
select nome, informacoesExtras from aluno
where informacoesExtras->>'telefone' = '84581151';

drop index idxJSON;


--------------------------------------------------------------------
-- Para ver os índices já criados:
SELECT tablename, indexname, indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;








