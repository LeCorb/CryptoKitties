import "./Ownable.sol";

pragma solidity 0.5.12;

contract ERC20 is Ownable {

    mapping (address => uint256) private _balances;

    uint256 private _totalSupply;

    string private _name;
    string private _symbol;
    uint8 private _decimals;

        constructor (string memory name, string memory symbol) public {
        _name = name;
        _symbol = symbol;
        _decimals = 18;
    }


    function name() public view returns (string memory) {
    	return _name;
    }

    function symbol() public view returns (string memory) {
        return _symbol;
    }

    function decimals() public view returns (uint8) {
        return _decimals;
    }

    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }
    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    function mint(address account, uint256 amount) public onlyOwner {
        require (account != address(0), "ERC20 : mint to the zero address");
        
        _totalSupply = _totalSupply + amount;
        _balances[account] += amount;
        
    }

    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(msg.sender != address(0), "transfert from the zero address")
        require(recipient != address(0), "transfert from the zero address")
        require(_balances[msg.sender] >= amount, "insufficient balance");
        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;
        
        return true;
    }
}
