# Direções e Eixos no Flexbox

O Flexbox é uma poderosa ferramenta do CSS para criar layouts flexíveis e responsivos. Ele organiza os itens em dois eixos principais:

## 1. Eixo Principal (Main Axis)
O eixo principal é definido pela propriedade `flex-direction`. Ele determina a direção em que os itens são organizados dentro do contêiner flexível.

### Valores de `flex-direction`:
- `row` (padrão): Os itens são organizados na direção da linha (da esquerda para a direita em idiomas LTR).
- `row-reverse`: Os itens são organizados na direção inversa da linha (da direita para a esquerda em idiomas LTR).
- `column`: Os itens são organizados na direção da coluna (de cima para baixo).
- `column-reverse`: Os itens são organizados na direção inversa da coluna (de baixo para cima).

## 2. Eixo Cruzado (Cross Axis)
O eixo cruzado é perpendicular ao eixo principal. Ele é usado para alinhar os itens no contêiner flexível e é controlado pela propriedade `align-items`.

### Propriedades relacionadas ao eixo cruzado:
- `align-items`: Alinha os itens ao longo do eixo cruzado.
- `align-content`: Alinha as linhas do contêiner flexível quando há múltiplas linhas.

## Exemplo de Código
```css
.container {
  display: flex;
  flex-direction: row; /* Define o eixo principal */
  align-items: center; /* Alinha os itens no eixo cruzado */
}
```

Compreender os eixos no Flexbox é essencial para criar layouts bem estruturados e responsivos.