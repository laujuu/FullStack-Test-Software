import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';

function CategoryBtn() {
  return (
    <DropdownButton id="dropdown-basic-button" title="Categoria">
      <Dropdown.Item href="#/action-1">Geladeira</Dropdown.Item>
      <Dropdown.Item href="#/action-2">TV</Dropdown.Item>
      <Dropdown.Item href="#/action-3">Celular</Dropdown.Item>
    </DropdownButton>
  );
}

export default CategoryBtn;