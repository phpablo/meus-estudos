
# 🧠 Padrão de Commits 

Este repositório contém um guia completo e prático sobre como criar mensagens minimalistas de commit organizadas, visuais e profissionais, usando **emojis**, **labels** e boas práticas de versionamento com Git e GitHub.



## ✍️ Exemplo de estrutura de commit

| Emoji | Prefixo (tag) | Corpo | Descrição | Rodapé |
| ----- | ----- | ----- | ----- | ----- |
| :bug: | fix: |  corrige retorno da funcao |  - corrige funcao getNome | Novo parâmetro recebido na função Resolvido Tarefa  #0035
| :sparkles: | feat: | adiciona nova funcinalidade | - nova funcao para filtrar pesquisa | Novos filtros de busca Tarefa  #0036
| :fire: | chore: | remove codigo não utilizado | - remove variaveis que nao sao usadas | Limpeza de codigo desnecessario  Resolvido Tarefa  #0037
| :package: | chore: | manutencao de dependecias | - adiciona nova dependencia X | Nova dependencias pro NodeJS  Resolvido Tarefa  #0037
| :wrench: | chore: | manutencao de funcionalidade | - Inclui paramêtro na funcaoGetNome | O parâmetro agora é NULL caso não for passado | Resolvido Tarefa  #0037
| :recycle: | refactor: | refatora funcao getNome | - não precisa mais de um parâmetro via get | Removeu codigo antigo e com muitas condições aninhadas | Resolvido Tarefa  #0038
| :art: | style: | novo layout da foto de perfil | - adiciona novo layou para seção de perfil | Layout atualizado com cores da empresa | Resolvido Tarefa  #00359
| :pencil: | doc: | add documentacao da funcao | - documenta a funcao principal da sessão de perfil | Seguir a documentacao de cada funcao para evitar redundância | Resolvido Tarefa  #00359
| :white_check_mark: | test: | aprovado testes de verificacao | - feito teste de validação de token | Teste aprova aceitação de strings na function getNome sem o ID int | Resolvido Tarefa  #00359

## ✍️ Exemplo de um commit completo

```
🎨 style: adiciona novo layout com cor identidade visual da empresa
- Remove codigo hexadecimal de cores antigas
- Adiciona cores padrão conforme a identidade da empresa na área de perfil do usuario

As cores seguem o mesmo modelo das outras áreas do sistema para manter fidelidade ao design
```


## 🧠 Boas práticas

- Use presente do indicativo: adiciona, cria, corrige, refatora.

- Seja objetivo e direto: até 80 caracteres é o ideal.

- Use a área entre parênteses quando fizer sentido: (logica), (readme), (api).

- Commits pequenos e frequentes são melhores do que grandes e genéricos.

### 👨‍💻 Autor

**Pablo Henrique**
Estudante de Análise e Desenvolvimento de Sistemas
UFCA — Universidade Federal do Cariri
Estudante de Engenharia de Software pela Universidade União das Américas Descomplica