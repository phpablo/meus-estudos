# Align Content in Flexbox  

The `align-content` property in CSS is used to control the alignment of a flex container's lines when there is extra space in the cross-axis. This property is only effective when the flex container has multiple lines (i.e., when `flex-wrap` is set to `wrap` or `wrap-reverse`).

## Syntax  
```css
align-content: flex-start | flex-end | center | space-between | space-around | space-evenly | stretch;
```

## Values  
- **`flex-start`**: Lines are packed at the start of the cross-axis.  
- **`flex-end`**: Lines are packed at the end of the cross-axis.  
- **`center`**: Lines are packed in the center of the cross-axis.  
- **`space-between`**: Lines are evenly distributed, with the first line at the start and the last line at the end.  
- **`space-around`**: Lines are evenly distributed with equal space around them.  
- **`space-evenly`**: Lines are evenly distributed with equal space between and around them.  
- **`stretch`** (default): Lines stretch to fill the available space in the cross-axis.  

## Example  
```html
<div class="container">
  <div class="item">1</div>
  <div class="item">2</div>
  <div class="item">3</div>
  <div class="item">4</div>
  <div class="item">5</div>
  <div class="item">6</div>
</div>

<style>
  .container {
    display: flex;
    flex-wrap: wrap;
    align-content: space-between;
    height: 200px; /* To demonstrate extra space */
  }
  .item {
    flex: 0 0 30%;
    height: 50px;
    background: lightblue;
    margin: 5px;
    text-align: center;
    line-height: 50px;
  }
</style>
```

In this example, the `align-content: space-between;` ensures that the lines of items are evenly distributed with space between them in the cross-axis.

## Notes  
- The `align-content` property does not affect single-line flex containers.  
- It works in conjunction with `flex-wrap` and the height of the container to determine the layout.  
