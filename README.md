# Loteria
Aplicação cliente-servidor de uma loteria em Python

##Tecnologias:
	Python 2.7
	MySQL 5.5
	PyQT 4
	Protocolo TCP

##Pré-requisitos:
	Instalar a biblioteca PyQT para o correto funcionamento da parte gráfica do sistema.
		sudo apt-get install python-qt4

##Base de dados:
	create database loteria;

	create table aposta (
		id_aposta int auto_increment,
		campo1 int,
		campo2 int,
		campo3 int,
		campo4 int,
		campo5 int,
		campo6 int,
		id_pessoa int,
		foreign key (id_pessoa) references pessoa (id_pessoa),
		primary key (id_aposta)
	);

	create table pessoa (
		id_pessoa int auto_increment,
		nome varchar(90),
		idade int,
		cpf varchar(20),
		endereco varchar(160),
		login varchar(30),
		senha varchar(45),
		email varchar(90),
		cartao varchar(50),
		conta varchar(10),
		primary key(id_pessoa)
	);

####Neto Deolino
<ol>
    <li> linkedin.com/in/netodeolino </li>
    <li> http://netodeolino.github.io </li>
</ol>