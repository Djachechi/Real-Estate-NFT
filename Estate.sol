pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/ownership/Ownable.sol";
import './EstateAuction.sol';

contract Estate is ERC721, Ownable {
    constructor() ERC721("Estate", "ACS") public {}

    // cast a payable address for the Martian Development Foundation to be the beneficiary in the auction
    // this contract is designed to have the owner of this contract (foundation) to pay for most of the function calls
    // (all but bid and withdraw)


    address payable foundation_address = address(uint160(owner()));

    mapping(uint => EstateAuction) public auctions;
    
    
    
    function registerproperty(string memory TokenURI) public payable onlyOwner {
        uint _id = totalSupply();
        _mint(msg.sender, _id);
        _setTokenURI(_id, TokenURI);
        createAuction(_id);
    }

    function createAuction(uint token_id) public onlyOwner {
       auctions[token_id] = new EstateAuction(foundation_address);
    }


    function endAuction(uint token_id) public onlyOwner {
        require(_exists(token_id), "Blue Print not available");
        EstateAuction auction = auctions[token_id];
        auction.auctionEnd();
        safeTransferFrom(owner(), auction.highestBidder(), token_id);
    }

    function getAuction(uint token_id) public view returns(EstateAuction auction) {
       EstateAuction auction = auctions[token_id];
        return auction.getAuction();
        
    }

    function auctionEnded(uint token_id) public view returns(bool) {
         EstateAuction auction = auctions[token_id];
          return auction.ended();
    }

    function highestBid(uint token_id) public view returns(uint) {
       EstateAuction auction = auctions[token_id];
        return auction.highestBid(); 
    }

    function pendingReturn(uint token_id, address sender) public view returns(uint) {
      EstateAuction auction = auctions[token_id];
        return auction.pendingReturn(sender);
    }

    function bid(uint token_id) public payable {
        EstateAuction auction = auctions[token_id];
        auction.bid.value(msg.value)(msg.sender);
    }

}
