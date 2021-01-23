pragma solidity 0.5.0;

contract Test1 {


  struct TestStruct {
    uint [] numbers;
  }

  mapping (address => TestStruct) testing;
  
  function addNumbers (uint _newNumber) public {
      testing[msg.sender].numbers.push(_newNumber);
  }

  function getNumbers () public view returns (uint[] memory){
    return testing[msg.sender].numbers;
        }
  }
 