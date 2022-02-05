pragma solidity ^0.5.5;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract EstateRegistry is ERC721Full {
    constructor() public ERC721Full("EstateRegistry Token", "ACS") {}

    struct Property {
        string name;
        string Location;
        string PropertyHistory;
        uint256 appraisalValue;
    }

    mapping(uint256 => Property) public Portfolio;

    event Appraisal(uint256 tokenId, uint256 appraisalValue, string reportURI);

    function registerProperty(
        address owner,
        string memory name,
        string memory PropertyHistory,
        string memory Location,
        uint256 initialAppraisalValue,
        string memory tokenURI
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();

        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        Portfolio[tokenId] = Property(name, PropertyHistory, Location, initialAppraisalValue);

        return tokenId;
    }

    function newAppraisal(
        uint256 tokenId,
        uint256 newAppraisalValue,
        string memory reportURI
    ) public returns (uint256) {
        Portfolio[tokenId].appraisalValue = newAppraisalValue;

        emit Appraisal(tokenId, newAppraisalValue, reportURI);

        return Portfolio[tokenId].appraisalValue;
    }
}
