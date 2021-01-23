pragma solidity 0.5.0;

contract Test1 {

  uint256 private id;

  constructor ()
  public
  {
    id = 0;
  }

  struct Person {
    string name;
    uint8 id;
    uint256 registrationTimeStamp;
  }

  mapping (address => Person) people;
  

  function createPerson (string memory _name, uint8 memory _id, uint256 memory _registrationTimeStamp ) public {
        
        //This creates a person
        Person memory newPerson;
        newPerson.name = _name;
        newPerson.id = _id;
        id++;
        _registrationTimeStamp = now
        newPerson.registrationTimeStamp = _registrationTimeStamp;
        
  }
}