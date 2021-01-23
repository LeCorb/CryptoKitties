pragma solidity 0.5.12;

contract Test0 {
    
    struct Owner {
        address creator;
        bool isOwner;
    }
    
    mapping (address => Owner) public owners;
    
    function setOwner (address _newOwner) public {
     owners[_newOwner].isOwner = true;
    }
    
    function getOwner (address _owner) public view returns (bool) {
        return owners[_owner].isOwner;
    }
            
}
    