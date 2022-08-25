-- consulta toda a tabela
SELECT * FROM estados

-- consulta valores específicos
SELECT sigla, nome as 'Nome do Estado' FROM estados
WHERE REGIAO = 'SUL'

select
    nome as 'Nome',
    regiao as 'Região',
    populacao 'População (Mi)'
from
    estados
where
    populacao >= 10
order by
    populacao desc