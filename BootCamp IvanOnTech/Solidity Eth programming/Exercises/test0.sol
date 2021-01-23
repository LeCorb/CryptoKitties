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
    
    function getOwner (address) public {
      for (i=0; i<=owners.length;i++){
        if (address == owners[i].creator){
            if (owners[i].isOwner == true){
                return Owner.isOwner;
            }
        }  
        
      }
    }
}
    