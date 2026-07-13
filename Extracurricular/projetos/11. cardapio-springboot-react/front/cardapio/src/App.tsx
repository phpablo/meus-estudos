import {useState} from 'react'
import './App.css'
import { Cards } from './components/card/cards';
import type { FoodData } from './interface/foodData';

function App() {
  const data: FoodData[] = [];

  return (
    <div className="container">
      <h1>Cardápio</h1>
      <div className='card-grid'>
        {data.map(foodData => 
          <Cards 
            price={foodData.price} 
            title={foodData.title} 
            image={foodData.image}
          />
        )}
      </div>
    </div>
  )
}

export default App
