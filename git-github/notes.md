# Git
Sistema de controle de versão distribuido
Open source
Leve e rápido
Criado por Linus Torvalds

# Github
Plataforma de hospedagem de código para controle de versão com git, e colaboração;
Criado em 2008 por Chris Wanstrath, J. Hyett, Tom Preston-Werner e Scott Chacon;
Em 2018 foi comprada pela Microsoft por US $ 7,5 bilhões.

# Comandos
mkdir - cria diretorio
cd nome do repo - entra no repositório
ls - lista conteudo da pasta
cd .. - volta uma pasta
stage - área de preparação

touch README.md - cria o arquivo README.md no repositório local
https://readme.so/pt/editor

 
git init - inicializa um repositório
git add . manda todos os arquivos para a área de preparação
git add <nomeDoArquivo> manda o arquivo para a área de preparação
git clone + url - clona repositório da url
cat config - mostra o core do repositório
git commmit -m -> cria uma nova versão do projeto;
git pull -> "puxa" as alterações do repositório remoto para o local(busca e mescla);
git push -> "empurra" as alterações do repositório local para o remoto;
git log - mostra o arquivo comitado 
.getkeep - para que o git reconheça um diretório vazio


https://docs.github.com/pt/get-started

Desfazendo uma alteraçãop no repositório
Depois de comitado
git restore

Alterando o nome  do ultimo commit
git commit --amend -m "nova mensagem"


Desfazendo o último commit
git reset --soft + hashDoUltimoCommit
git reset --mixed + hashDoUltimoCommit
git reset --hard +  hashDoUltimoCommit

git fetch - baixa as alterações do remoto sem mesclar com o local
git diff - mostra as diferenças de uma branch

git clone + url --branch + nomeBranch - clonar uma branch específica de um repositório


Histórico detalhado
git reflog


## Branches
É uma ramificaçao do projeto;
Ponteiro móvel para o commit no histórico do repositório;
Quando você cria uma nova branch a partir de outra eistente, a nova se inicia apontando para o mesmo commit da branch que estava quando foi criada;



# Markdown
# Titulo
## Subtitulo
- [Link](urldolink)
'''
caixa de codigo
'''
| Separa | em | tabelas |

















