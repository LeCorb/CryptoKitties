import "./People.sol";
pragma solidity 0.5.12;

contract Workers is People{
	struct Worker {
      uint worker_salary;
    }

	mapping (address => uint) public salary;
	
	function createWorker(string memory name, uint age, uint height, uint worker_salary) public payable {

		require (age <= 75, "Age needs to be below 75");
		createPerson(name, age, height);
		salary[msg.sender] += worker_salary;
	}

	address[] private worker_salary;	
}