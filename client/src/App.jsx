import { useState } from 'react'
import WebBtn from './components/WebBtn';
import CategoryBtn from './components/CategoryBtn';
import SearchForm from './components/SearchForm';
import InputSearch from './components/InputSearch';


import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css'


function App() {
  const [site, setSite] = useState(null); 
  const [category, setCategory] = useState(null);

  const handleSiteChange = (site) => {
    setSite(site);
  };

  const handleCategoryChange = (category) => {
    setCategory(category);
  };

  return (
    <div className="App">
      <h1>Raspa Web</h1>
      <div className='SearchCard'>
        <WebBtn onSelect={handleSiteChange} />
        <CategoryBtn onSelect={handleCategoryChange} />
      </div>
      <div className='inpSearch'>
      <InputSearch />
      </div>
      <SearchForm site={site} category={category} />
      <p className="read-the-docs">
        Selecione um filtro para iniciar ou alterar a pesquisa
      </p>
    </div>
  )
}

export default App;
