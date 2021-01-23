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
    uint256 id;
    uint256 registrationTimeStamp;
  }

  mapping (address => Person) public people;
  

  function createPerson (string memory _name) public {
    people[msg.sender].name = _name;
    people[msg.sender].id = id; 
    people[msg.sender].registrationTimeStamp = now;
    id = id + 1;
  }
  
  function getPerson(address ins) public view returns (string memory, uint256, uint256){
      return (people[ins].name, people[ins].id, people[ins].registrationTimeStamp);
  }
}