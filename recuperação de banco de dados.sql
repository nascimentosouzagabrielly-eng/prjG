create database Escola;

use Escola;

create table aluno (
    id_aluno int not null auto_increment,
    nome varchar(100) not null,
    data_nascimento date,
    email varchar(100),
    primary key (id_aluno)
);

create table disciplina  (
    id_disciplina int not null auto_increment,
    nome varchar(100) not null,
    carga_horaria int,
    primary key (id_disciplina)
);

create table aluno_disciplina (
    id_aluno int not null,
    id_disciplina int not null,
    
    primary key (id_aluno, id_disciplina),
    
    foreign key (id_aluno)
        references aluno(id_aluno),
        
    foreign key (id_disciplina)
        references disciplina(id_disciplina)
);