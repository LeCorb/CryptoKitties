import "./People.sol";
pragma solidity 0.5.12;

contract Workers is People{
	
	struct Worker {
      
      address theBoss;
      uint worker_salary;
      
    }

	mapping (address => uint) public salary;
	
	
	
	function createWorker(string memory name, uint age, uint height, address theBoss, address _theBoss, uint worker_salary) public payable {

		require (age <= 75, "Age needs to be below 75");
		createPerson(name, age, height);
		salary[msg.sender] += worker_salary;
		theBoss = _theBoss;
	}

	

	function fireWorker(address _toFire, address theBoss) public {
      	require( msg.sender == theBoss, "You are not the Boss to fire him !");
      	require(_toFire != msg.sender, "You're the boss, You cannot fire yourself !");
      	deletePerson(_toFire);
      	delete salary[_toFire];
   }
}