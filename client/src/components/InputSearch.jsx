import { useState } from 'react';
import Form from 'react-bootstrap/Form';

function InputSearch({ onKeywordChange }) {
  const [searchTerm, setSearchTerm] = useState('');

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      onKeywordChange(searchTerm);
      event.preventDefault();
      setSearchTerm('');
    }
  };

  return (
    <Form>
      <Form.Group className="mb-3">
        <Form.Control
          type="text"
          placeholder="Pesquisar"
          value={searchTerm}
          onChange={(event) => setSearchTerm(event.target.value)}
          onKeyDown={handleKeyDown}
        />
      </Form.Group>
    </Form>
  );
}

export default InputSearch;
