pragma solidity ^0.4.21;
pragma experimental ABIEncoderV2;
//pragma experimental ABIEncoderV2
contract Wiki{
    
    //string[] Title = new string[](10);
    //string[] ipfs_hash = new string[](10);
    string[]  Title;
    
    //address payable owner;
    struct Article{
        
        string[] ipfs_hash;
        address[] author_address;
        uint256 [] timestamp;
        
        // uint256 [] timestamp;
    }
    struct Author{
        
        uint256 reputation;
        bool exists;
    }
    
    mapping(string=> Article) const_article_title; //title to author
    mapping(address => Author) manage_reputation;
    
    address public contract_address = address(this);
   
    event article_dist_calc(
        string []  ipfs_hash,
        address []  author_address,
        uint256 [] timestamp
        
    );
     
    
    function new_article(string memory _Title, string memory _hash) public  {
        
        Title.push(_Title);
        const_article_title[_Title].ipfs_hash.push(_hash);
        const_article_title[_Title].author_address.push(msg.sender);
        const_article_title[_Title].timestamp.push(now);
        if (manage_reputation[msg.sender].exists == false)
        {
            manage_reputation[msg.sender].reputation = 0;
            manage_reputation[msg.sender].exists = true;
        }
       
        emit article_dist_calc(const_article_title[_Title].ipfs_hash, const_article_title[_Title].author_address,  const_article_title[_Title].timestamp);
    }
    
    function getTitles()public view returns(string []  memory ){
         return Title;
    }
    function getHashes(string memory _Title)public view returns(string []  memory){
         return const_article_title[_Title].ipfs_hash;
    }
    function getAddress(string memory _Title)public view returns(address []  memory){
         return const_article_title[_Title].author_address;
    }
    function getTimestamps(string memory _Title)public view returns(uint256 []  memory){
         return const_article_title[_Title].timestamp;
    }
    
    function getReputation(address author_address)public view returns(uint256 ){
         return manage_reputation[author_address].reputation;
    }
    
    function ReputationUpdate(address author_address, uint256 author_reputation )public {
        
       
        manage_reputation[author_address].reputation = author_reputation;
        
    }
    
    
   
    
    // function author_added(address _author_address) public view returns(bool isIndeed) {
    //     return manage_reputation[_author_address].exists;
    // }

    // function addAuthor(address _author_address) public returns(bool success) {
    //     require(!author_added(_author_address));
    //     manage_reputation[_author_address].reputation = 0;
    //     manage_reputation[_author_address].exists = true;
    //     return true;
    // }
    
    function update_reputation(address _author_address, uint256 value) external payable
    {
        
        manage_reputation[_author_address].reputation = manage_reputation[_author_address].reputation + value;
        // return manage_reputation[_author_address].reputation;
    }
    
    
    function send_eth () external payable{  //sending ether from account to smart contract
      
    }
    
    function gasprice() payable public returns (uint256)      //transfer gas price to author
    {
        uint cost;
        cost = tx.gasprice * gasleft();
        msg.sender.transfer(cost);
        
    }
    
    function get_account_balance() external view returns (uint){
        
        return (msg.sender.balance);
    }
    
    function get_contract_balance() external view returns (uint){
        
        return (address(this).balance);
    }
    
}


