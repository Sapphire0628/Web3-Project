// Help Truffle find `TruffleTutorial.sol` in the `/contracts` directory
const TestContract = artifacts.require("TestContract");

module.exports = function(deployer) {
  // Command Truffle to deploy the Smart Contract
  deployer.deploy(TestContract);
};