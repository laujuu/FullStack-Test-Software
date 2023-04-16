import { useState, useEffect } from 'react';
import axios from 'axios';
import defaultImage from '../assets/defaultImage.png';
import Button from 'react-bootstrap/Button';

function SearchForm({ category, site, keyword }) {
  const [results, setResults] = useState([]);
  console.log('results', results)
  
  console.log('site', site)
  console.log('categoria', category);
  console.log('search', keyword);

  
  useEffect(() => {
    if (category && site) {
      let url;
      if (keyword) {
        url = `http://127.0.0.1:5000/search_${site}_by_keyword?category=${category}&keyword=${keyword}`;
      } else {
        url = `http://127.0.0.1:5000/search_${site}_by_category?category=${category}`;
      }
      axios.get(url)
        .then(response => setResults(response.data))
        .catch(error => console.error(error));
    }
  }, [category, site, keyword]);

  return (
    <div>
      {results.map(result => (
        <div key={result.id}>
          {result.image === 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7' ?
            <img src={ defaultImage } alt={ result.title } /> :
            <img src={ result.image } alt={ result.title } />
          }
          <h2>{result.title}</h2>
          <p>{result.description}</p>
          <p>Preço: {result.price}</p>
          <Button 
          href={result.link} 
          target="_blank" 
          rel="noopener noreferrer"
          variant="success"
          >Ir a web</Button>
          <hr />
        </div>
      ))}
    </div>
  );
}

export default SearchForm;
