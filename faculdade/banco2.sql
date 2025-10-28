.open infnet.db
.mode table

drop table if exists aluno;
drop table if exists endereco;
drop table if exists email;
drop table if exists disciplina;
drop table if exists aluno_disciplina;

PRAGMA foreign_keys = ON;

create table aluno(
	id_aluno integer primary key autoincrement,
	nome char(50) not null,
	telefone char(20)
);

insert into aluno values(null, 'Arthur', '11111-1111');
insert into aluno values(null, 'Igor', '22222-2222');
insert into aluno values(null, 'Lucas', '33333-3333');
insert into aluno values(null, 'LP', '44444-4444');

create table endereco(
	id_endereco integer primary key autoincrement,
	rua char(50) not null,
	-- outros atributos
	id_aluno int not null unique, -- Relacionamento um para um
	foreign key (id_aluno) references aluno(id_aluno) ON DELETE CASCADE
);

insert into endereco values(null, 'Rua do Arthur', 1);
-- insert into endereco values(null, 'Rua do Arthur 2', 1); Erro!!!!!!!
insert into endereco values(null, 'Rua do Lucas', 3);
insert into endereco values(null, 'Rua do LP', 4);

create table email(
	id_email integer primary key autoincrement,
	email char(50) not null,
	id_aluno int not null, -- Relacionamento um para muitos
	foreign key (id_aluno) references aluno(id_aluno) ON DELETE CASCADE
);

insert into email values(null, 'arthur@gmail.com', 1);
insert into email values(null, 'arthur@infet.com', 1);
insert into email values(null, 'igor@gmail.com', 2);
insert into email values(null, 'lp@gmail.com', 4);

create table disciplina(
	id_disciplina integer primary key autoincrement,
	nome char(30) not null
	-- outros atributos
);

insert into disciplina values(null, 'SQL-2');
insert into disciplina values(null, 'Python-2');
insert into disciplina values(null, 'PB-FD');
insert into disciplina values(null, 'Java');

create table aluno_disciplina(
	id_aluno int not null,
	id_disciplina int not null,
	primary key (id_aluno, id_disciplina),
	foreign key (id_aluno) references aluno(id_aluno) ON DELETE CASCADE,
	foreign key (id_disciplina) references disciplina(id_disciplina) ON DELETE CASCADE
);

insert into aluno_disciplina values(1, 1);
insert into aluno_disciplina values(1, 2);
insert into aluno_disciplina values(1, 3);
insert into aluno_disciplina values(3, 3);
insert into aluno_disciplina values(4, 4);

-- delete from aluno where id_aluno = 4;
-- delete from disciplina where id_disciplina = 4;

select * from aluno;
select * from endereco;
select * from email;
select * from disciplina;
select * from aluno_disciplina;


