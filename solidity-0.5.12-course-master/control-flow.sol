pragma solidity 0.5.12;

contract HelloWorld{

    struct Person {
      uint id;
      string name;
      uint age;
      uint height;
      bool senior;
    }

    mapping (address => Person) private people;

    function createPerson(string memory name, uint age, uint height) public {
        address creator = msg.sender;

        //This creates a person
        Person memory newPerson;
        newPerson.name = name;
        newPerson.age = age;
        newPerson.height = height;

        if(age >= 65){
           newPerson.senior = true;
       }
       else{
           newPerson.senior = false;
       }

        people[creator] = newPerson;
    }
    function getPerson() public view returns(string memory name, uint age, uint height, bool senior){
        address creator = msg.sender;
        return (people[creator].name, people[creator].age, people[creator].height, people[creator].senior);
    }
}
