pragma solidity 0.5.12;

contract People{

    struct Person {
      uint id;
      string name;
      address creator;
      uint age;
      uint height;
      bool senior;
    }

    Person[] private people;
    mapping (address => uint) nbofpeople;
    address [] public testArray;

    function createPerson(string memory name, uint age, uint height) public {
        //This creates a person
        Person memory newPerson;
        newPerson.id = people.length;
        newPerson.creator = msg.sender;
        newPerson.name = name;
        newPerson.age = age;
        newPerson.height = height;
        nbofpeople[msg.sender] = nbofpeople[msg.sender] + 1;

        if(age >= 65){
           newPerson.senior = true;
        }
        else{
           newPerson.senior = false;
        }
        people.push(newPerson); 
    }

    function getPerson(uint ins) public view returns (string memory, uint, uint,uint,address, bool){
      return (people[ins].name, people[ins].age, people[ins].height, people[ins].id, people[ins].creator, people[ins].senior);
        
    }

}    