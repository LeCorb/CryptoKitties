pragma solidity 0.5.12;

contract HelloWorld{

    struct Person {
      uint id;
      string name;
      uint age;
      uint height;
      bool senior;
    }

    event personCreated(string name, bool senior);
    event personUpdated(uint id, string name, uint age, uint height, bool senior);

    mapping (address => Person) private people;

    function createPerson(string memory name, uint age, uint height) public {
        address creator = msg.sender;
        Person memory newPerson;
        
            uint oldId = people[msg.sender].id;
            string memory oldName = people[msg.sender].name;
            uint oldAge = people[msg.sender].age;
            uint oldHeight = people[msg.sender].height;
            bool oldSenior = people[msg.sender].senior;
            
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
        
        
        if (oldHeight == 0){
            emit personCreated(people[creator].name, people[creator].senior); 
        }else{
            emit personUpdated(oldId, oldName, oldAge, oldHeight, oldSenior); 
        }
            
        }
    
    
    function getPerson() public view returns(string memory name, uint age, uint height, bool senior){
        address creator = msg.sender;
        return (people[creator].name, people[creator].age, people[creator].height, people[creator].senior);
    }
}
