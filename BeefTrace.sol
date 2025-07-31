// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BeefTrace {
    struct EventLog {
        string description;
        uint timestamp;
        string actor;
    }

    EventLog[] public logs;

    event LogAdded(string description, uint timestamp, string actor);

    function addEvent(string memory _description, string memory _actor) public {
        logs.push(EventLog(_description, block.timestamp, _actor));
        emit LogAdded(_description, block.timestamp, _actor);
    }

    function getEvent(uint index) public view returns (string memory, uint, string memory) {
        EventLog memory log = logs[index];
        return (log.description, log.timestamp, log.actor);
    }

    function getTotalEvents() public view returns (uint) {
        return logs.length;
    }
}
