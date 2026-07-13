# Anatomia dos Itens Flexíveis do Flexbox

O Flexbox é uma poderosa ferramenta para criar layouts flexíveis e responsivos. Aqui está uma visão geral da anatomia dos itens flexíveis:

## Propriedades dos Itens Flexíveis

1. **`order`**  
  Define a ordem dos itens no contêiner flexível. O valor padrão é `0`. Itens com valores menores aparecem antes.

  ```css
  .item {
     order: 1;
  }
  ```

2. **`flex-grow`**  
  Controla o quanto um item pode crescer em relação aos outros. O valor padrão é `0` (não cresce).

  ```css
  .item {
     flex-grow: 2;
  }
  ```

3. **`flex-shrink`**  
  Define o quanto um item pode encolher em relação aos outros. O valor padrão é `1`.

  ```css
  .item {
     flex-shrink: 0;
  }
  ```

4. **`flex-basis`**  
  Especifica o tamanho inicial do item antes de distribuir o espaço restante. Pode ser definido em pixels, porcentagem, etc.

  ```css
  .item {
     flex-basis: 200px;
  }
  ```

5. **`flex`**  
  É uma abreviação para `flex-grow`, `flex-shrink` e `flex-basis`. Exemplo:

  ```css
  .item {
     flex: 1 1 100px; /* grow, shrink, basis */
  }
  ```

6. **`align-self`**  
  Permite alinhar individualmente um item, sobrescrevendo o alinhamento definido pelo contêiner.

  ```css
  .item {
     align-self: center;
  }
  ```

## Exemplo Prático

```html
<div class="container">
   <div class="item">Item 1</div>
   <div class="item">Item 2</div>
   <div class="item">Item 3</div>
</div>

<style>
   .container {
      display: flex;
   }
   .item {
      flex: 1;
   }
</style>
```

Neste exemplo, os itens terão tamanhos iguais, pois o valor de `flex` está configurado como `1`.
