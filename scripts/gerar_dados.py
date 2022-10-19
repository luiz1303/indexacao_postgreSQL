# -----------------------------------------------------------------------------
# Script para geração de dados randômicos - Banco de Dados II - UTFPR-PB
# Desenvolvido por Luiz Henrique Birck Vicari e Luiz Ricardo Brumati De Lima
# -----------------------------------------------------------------------------

import string
from random import choice, randint

lista_nomesInseridos = list ()
lista_nomeMaeInseridos = list ()

lista_nomes = ['Luiz', 'Maria', 'Miguel','Heitor','Juliana','Julia','Leticia','Heloisa','Roberta','Francisco','Henrique','Roberto','Pedro','Gustavo','Gabriel','Antonio',
'Samuel','Caio','Joao','Heitor','Arthur','Clara','Juliana','Sofia','Alice','Lara','Raquel','Laura','Fabiola','Helena','Beatriz','Carlos','Daniel','Andre','Fabio','Gabriela',
'Raimundo','Geovana','Ana','Sandra','Thais','Tales','Lucas','Henrique','Livia','Leonidas','Afonso','Marcio','Thiago','Diego','Manuel','Cesar','Eliane','Mariane', 'Jose','Miguel','Peter','Ives','Marcelo','Rafael','Paulo','Marcos','Bruno','Eduardo','Felipe','Leonardo','Manoel','Edson','Jorge','Matheus','Mateus','Alexandre','Claudio','Luis','Julio','Alex','Luciano','Vera','Francisca','Adriana','Juliana','Marcia','Marcela','Ana','Patricia','Cristiane','Cristina','Camila','Amanda','Bruna','Jessica','Luciana','Beatriz','Vanessa','Luana','Jaqueline','Daniela','Carla','Natalia','Simone','Eliane','Rafaela','Renata','Rafaela','Angela','Andrea','Regina','Luzia','Joana','Daiane','Isabela','Isabel','Alessandra','Sueli','Marlene','Aparecida','Rosa','Rosangela']

lista_cidade = ['Campo Grande','Alta Floresta','Sinop','Fortaleza','Mossoro','Belem','Altamira','Guarulhos','Ribeirao Preto','Balneario','Chapeco','Itapema','Laranjeiras', 'Limoeiro do norte','Aracati','Pato Branco', 'Curitiba', 'Ponta Grossa', 'Coronel Vivida', 'Florianopolis', 'Cascavel', 'Castro', 'Joinville', 'Maringa', 'Francisco Beltrao', 'Sao Paulo', 'Campinas', 'Porto Alegre', 'Gramado', 'Rio de Janeiro', 'Ouro Preto','Foz do Iguacu','Salvador','Maceio','Blumenal','Natal','Olinda','Tiradentes']

lista_estado = ['AC','AL','AP','AM','BA','CE','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']

lista_nome_mae = ['Helena', 'Alice', 'Laura', 'Manuela', 'Sofia', 'Isabela', 'Luisa', 'Heloisa', 'Cecilia', 'Antonia', 'Livia', 'Ester', 'Sarah', 'Lara', 'Mariana', 'Catarina', 'Agata', 'Claudia', 'Maria', 'Odete','Eleni','Roberta','Julia','Leticia','Gabriela','Elizangela','Cristiane','Vera','Ailda','Maria Clara','Luana','Geovana','Meire', 'Regina','Maria antonieta','Micaela','Michele','Michelle','Teodora','Teia','Elena','Izabel','Gabrielle','Veracia','Oseia','Esther','Sara','Iara','Leopolda','Giovana','Meira','Agatha','Camilly','Camile','Kemela','Sandra','Adriane','Juliane','Marcieli','Angelica','Daiana', 'Daiane']

lista_curso = ['Administracao','Agronomia','Ciencias Contabeis','Comercio Exterior','Letras','Economia','Gestao ambiental','Seguranca do trabalho','Historia','Fisica','matematica','Antropologia','Teologia','Quimica','Engenharia eletrica','Engenharia da computacao','Engenharia Civil','Direito','Medicina','Enfermagem','Educacao Fisica','Jornalismo','Publicidade e propaganda','design','Cinema','Fotografia','Engenharia de producao','Engenharia de Software','Geogragia','Geologia','Pedagogia','Ciencias Naturais','Arqueologia','Botanica','Oceanografia','Metereologia','Analise e Desenvolvimento de Sistemas','Tecnologia da Informacao','Sistemas de Informacao','Biologia','Estetica','Biotecnologia','Farmacia','Fisioterapia','Gastronomia','Turismo']

lista_nome_materia = ['Calculo 1', 'Calculo 2', 'Calculo 3', 'Calculo numerico', 'Fisica 1', 'Fisica 2', 'Fisica 3', 'Banco de dados 1', 'Banco de dados 2', 'Sistemas de Controle 1', 'Sistemas de Controle 2', 'Controle digital', 'Eletronica A', 'Eletronica B', 'Projeto de algoritmos', 'Libras','Ingles','Espanhol','Quimica','Biologia','Filosofia','Etica','Sistemas de Comunicacao','Qualidade de Vida','Esportes Coletivos','Ciencias do Ambiente','Historia','Geometria Analitica','Algebra Linear','Sinais e Sistemas','Direito Constitucional','Desenho Tecnico','Zoologia','Gestao Ambiental','Empreendedorismo','Linguistica','Teoria da Literatura','Literatura Brasileira','Design','Computacao Grafica','Leitura Ocidental','Semantica','Morfologia e sintaxe','Direito Administrativo','Antropologia e Direito','Ciencia Politica','Mediacao e Arbitragem','Bioestatistica','Probabilidade','Anatomia','Enfermagem','Citologia','Farmacologia','Bioseguranca','Arquitetura e Urbanismo','Comunicacao e expressao','Concreto 1','Concreto 2','Construcao Civil','Elementos de Maquinas','Eletricidade e Magnetismo','Manutencao Industrial','Mecanica','Projeto de automacao','Projeto termico','Refrigeracao','Sistemas de Medicao']

lista_Ra = list()
for i in range(1000):
    RA = randint(10000000, 99999999)
    if RA in lista_Ra:
        while RA in lista_Ra:
            RA = randint(10000000, 99999999)
    lista_Ra.append(RA)
lista_data_nascimento = list()

for i in range(27):
    for y in range(11):
        for z in range(1980, 2000):
            lista_data_nascimento.append(f'{i+1}/{y+1}/{z}')

lista_idade = [i for i in range(18, 40)]

lista_periodo = [i for i in range(1, 10)]

lista_siglas = list()
for i in range(1000):
    sigla = f'{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}'
    if sigla in lista_siglas:
        while sigla in lista_siglas:
            sigla = f'{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}'
    lista_siglas.append(sigla)


lista_Depto = list()
for i in range(100):
    sigla = f'{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}'
    if sigla in lista_Depto:
        while sigla in lista_Depto:
            sigla = f'{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}'
    lista_Depto.append(sigla)

lista_ra_sigla_ano = list()
for i in range(1000):
    ra_sigla_ano = (choice(lista_Ra), choice(lista_siglas), randint(2010, 2020))
    if ra_sigla_ano in lista_ra_sigla_ano:
        while ra_sigla_ano in lista_ra_sigla_ano:
            ra_sigla_ano = (choice(lista_Ra), choice(lista_siglas), randint(2010, 2020))
    lista_ra_sigla_ano.append(ra_sigla_ano)


with open('xDiscip.txt', 'w') as arquivo:
    for i in range(1000):
        arquivo.write(f"INSERT INTO Discip (Sigla, Nome, SiglaPreReq, NnCred, Monitor, Depto) VALUES ('{lista_siglas[i]}', '{choice(lista_nome_materia)}', '{choice(lista_siglas)}', {randint(0, 99)}, {choice(lista_Ra)} , '{choice(lista_Depto)}');\n")

with open('xAluno.txt', 'w') as arquivo:
    for i in range(1000):
        nome = choice(lista_nomes)
        nome_mae = choice(lista_nome_mae)
    
        #Impede a repetição de nome e nome da mãe iguais em diferentes linhas da tabela
        count = 0
        if len(lista_nomesInseridos) > 0:
            for tempVar in lista_nomesInseridos:
                
                while nome == lista_nomesInseridos[count] and nome_mae == lista_nomeMaeInseridos[count]:
                    nome = choice(lista_nomes)
                    nome_mae = choice(lista_nome_mae)

                count = count+1
        lista_nomesInseridos.append(nome)
        lista_nomeMaeInseridos.append(nome_mae)

        arquivo.write(f"INSERT INTO Aluno (Nome, RA, DataNasc, Idade, NomeMae, Cidade, Estado, Curso, periodo) VALUES ('{nome}',{lista_Ra[i]}, '{choice(lista_data_nascimento)}', {choice(lista_idade)}, '{nome_mae}', '{choice(lista_cidade)}', '{choice(lista_estado)}', '{choice(lista_curso)}', {choice(lista_periodo)});\n")

with open('xMatricula.txt', 'w') as arquivo:
    for i in range(1000):
        arquivo.write(f"INSERT INTO Matricula (RA, Sigla, Ano, Semestre, CodTurma, NotaP1, NotaP2, NotaTrab, NotaFIM, Frequencia) VALUES ({lista_ra_sigla_ano[i][0]},'{lista_ra_sigla_ano[i][1]}',{lista_ra_sigla_ano[i][2]},'{choice((1, 2))}',{randint(1000, 2000)},{randint(0, 100) /10},{randint(0, 100) /10},{randint(0, 100) /10},{randint(0, 100) /10},{randint(0,100)});\n")
