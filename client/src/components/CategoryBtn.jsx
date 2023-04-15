import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';

function CategoryBtn(props) {
  const handleSelect = (category) => {
    props.onSelect(category);
  };

  return (
    <DropdownButton id="dropdown-basic-button" title="Categoria" onSelect={handleSelect}>
      <Dropdown.Item eventKey="geladeira">Geladeira</Dropdown.Item>
      <Dropdown.Item eventKey="tv">TV</Dropdown.Item>
      <Dropdown.Item eventKey="celular">Celular</Dropdown.Item>
    </DropdownButton>
  );
}

export default CategoryBtn;
