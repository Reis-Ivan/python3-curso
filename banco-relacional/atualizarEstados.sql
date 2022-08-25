-- importanteo o uso do WHERE
update `estados`
set nome = 'Maranhão'
where sigla = 'MA'

select nome from `estados` where sigla = 'MA'

update `estados`
set nome = 'Paraná',
    populacao = 11.32
WHERE sigla = 'PR'

select
    est.nome,
    est.sigla,
    est.populacao
from
    estados est
WHERE
    sigla = 'PR'