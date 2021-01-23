pragma solidity 0.5.12;

contract ERC20 {

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

    }

    function symbol() public view returns (string memory) {

    }

    function decimals() public view returns (uint8) {

    }

    function totalSupply() public view returns (uint256) {


    function balanceOf(address account) public view returns (uint256) {

    }

    function mint(address account, uint256 amount) public {

    }

    function transfer(address recipient, uint256 amount) public returns (bool) {

    }
}
