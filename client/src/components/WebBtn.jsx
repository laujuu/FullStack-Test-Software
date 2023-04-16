import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';

function WebBtn(props) {
  const handleSelect = (site) => {
    props.onSelect(site);
    console.log('selecionando site', site);

  };

  return (
    <DropdownButton id="dropdown-basic-button" title="Web" onSelect={handleSelect}>
      <Dropdown.Item eventKey="all">Todas</Dropdown.Item>
      <Dropdown.Item eventKey="meli">Mercado Livre</Dropdown.Item>
      <Dropdown.Item eventKey="buscape">Buscapé</Dropdown.Item>
    </DropdownButton>
  );
}

export default WebBtn;
