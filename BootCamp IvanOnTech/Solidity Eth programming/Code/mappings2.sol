pragma solidity 0.5.12;
pragma experimental ABIEncoderV2;

contract HelloWorld{
    
    struct Person{
        string name;
        uint age;
        uint height;
        
    }

    mapping(address => Person) private people;
    
    function createPerson(string memory name, uint age, uint height)public {
        address creator = msg.sender;
        
        //this creates a person
        Person memory newPerson;        
        newPerson.name = name;
        newPerson.age = age;
        newPerson.height = height;
        
        people[creator] = newPerson;
        
        //people.push(Person(people.length, name, age, height));  
    }
        
    function getPerson() public view returns(string memory name, uint age, uint height){
        address creator = msg.sender;
        return (people[creator].name, people[creator].age, people[creator].height);  
    }
    
}