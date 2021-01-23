pragma solidity 0.5.12;

contract HelloWorld{

    struct Person {
      uint id;
      string name;
      uint age;
      uint height;
      bool senior;
    }

    address public owner;

    event personCreated(string name, bool senior);
    event personUpdated(uint id, string name, uint age, uint height, bool senior);
    
    modifier onlyOwner(){
        require(msg.sender == owner);
        _; //Continue execution
    }

    constructor() public{
        owner = msg.sender;
    }

    mapping (address => Person) private people;
    address[] private creators;

    function createPerson(string memory name, uint age, uint height) public {
      require(age < 150, "Age needs to be below 150");
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
        
        
        if (stringsEqual(people[msg.sender].name, oldName)){
            emit personUpdated(oldId, oldName, oldAge, oldHeight, oldSenior);
        }else{
            emit personCreated(people[creator].name, people[creator].senior); 
        }
            
        }

        insertPerson(newPerson);
        creators.push(msg.sender);

        assert(
            keccak256(
                abi.encodePacked(
                    people[msg.sender].name,
                    people[msg.sender].age,
                    people[msg.sender].height,
                    people[msg.sender].senior
                )
            )
            ==
            keccak256(
                abi.encodePacked(
                    newPerson.name,
                    newPerson.age,
                    newPerson.height,
                    newPerson.senior
                )
            )
        );
        
    function stringsEqual(string storage _a, string memory _b) view internal returns (bool) {
        bytes storage a = bytes(_a);
        bytes memory b = bytes(_b); 
        if (a.length != b.length) 
        return false;
    }
    
    function insertPerson(Person memory newPerson) private {
        address creator = msg.sender;
        people[creator] = newPerson;
    }
    function getPerson() public view returns(string memory name, uint age, uint height, bool senior){
        address creator = msg.sender;
        return (people[creator].name, people[creator].age, people[creator].height, people[creator].senior);
    }
    function deletePerson(address creator) public onlyOwner {
       delete people[creator];
       assert(people[creator].age == 0);
   }
   function getCreator(uint index) public view onlyOwner returns(address){
       return creators[index];
   }

}
