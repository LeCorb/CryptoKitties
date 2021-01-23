pragma solidity 0.5.12;


contract Game{
    
    struct Player{
        
        uint gamesPlayed;
        uint8 w;
        uint8 l;
        bool isPlayer;
    }
    
    mapping(address => Player) public players; 
    
    
    function registerPlayer () public {
        players[msg.sender].isPlayer = true;
    }
    
    function removePlayer (address _toRemove) public {
        require (players[_toRemove].isPlayer == true, 'player not registered'); 
        require (msg.sender == _toRemove);
        delete(players[msg.sender]);
    }
    
    function play () public returns (bool) {
        require (players[msg.sender].isPlayer == true, 'player not registered');
        if (now % 2 == 0) {
            players[msg.sender].w = players[msg.sender].w + 1;
            return true;
        } else {
            players[msg.sender].l = players[msg.sender].l + 1;
            return false;
        }
    }
    
        
}