import { useState, useEffect } from 'react';
import axios from 'axios';

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
          <img src={result.image} alt={result.title} type="image/gif" />
          <h2>{result.title}</h2>
          <p>{result.description}</p>
          <p>Preço: {result.price}</p>
        </div>
      ))}
    </div>
  );
}

export default SearchForm;
