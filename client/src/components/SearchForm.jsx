import Form from 'react-bootstrap/Form';

function SearchForm() {
   return (
     <Form>
       <Form.Group className="mb-3">
         <Form.Control type="text" placeholder="Pesquisar" />
       </Form.Group>
     </Form>
   );
}

export default SearchForm;