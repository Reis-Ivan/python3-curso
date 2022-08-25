select * from `estados` where id = 29

insert into cidades
    (nome, area, estado_id)
values
    ('Campinas', 795, 29)

insert into cidades (nome, area, estado_id)
values ('Niterói', 133.9, 23)

insert into cidades (nome, area, estado_id)
values(
    'Caruaru',
    920.6,
    (select id from `estados` where sigla = 'PE')
)

INSERT INTO cidades
    (NOME, AREA, ESTADO_ID)
VALUES (
    'Juazeiro do Norte',
    248.2,
    (SELECT ID FROM `estados` WHERE SIGLA = 'CE')
)

select * from cidades 