import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';

function WebBtn() {
  return (
    <DropdownButton id="dropdown-basic-button" title="Web">
      <Dropdown.Item href="#/action-1">Todas</Dropdown.Item>
      <Dropdown.Item href="#/action-2">Mercado Livre</Dropdown.Item>
      <Dropdown.Item href="#/action-3">Buscapé</Dropdown.Item>
    </DropdownButton>
  );
}

export default WebBtn;