import Form from 'react-bootstrap/Form';
import '../App.css'

function InputSearch() {
   return (
     <Form>
       <Form.Group className="mb-3">
         <Form.Control type="text" placeholder="Pesquisar" />
       </Form.Group>
     </Form>
   );
}

export default InputSearch;