import { useState } from 'react'
import WebBtn from './components/WebBtn';
import CategoryBtn from './components/CategoryBtn';
import SearchForm from './components/SearchForm';

import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css'

function App() {

  return (
    <div className="App">
      <h1>Raspa Web</h1>
      <div className='SearchCard'>
        <WebBtn />
        <CategoryBtn />
      </div>
      <SearchForm />
      <p className="read-the-docs">
        Selecione um filtro para iniciar a pesquisa
      </p>
    </div>
  )
}

export default App
