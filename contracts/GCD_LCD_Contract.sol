// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract GCD_LCD {
    function GetGCD(uint num1, uint num2) public view returns (uint){
        return num2 > 0 ? GetGCD(num2, num1 % num2) : num1;
    }

    function GetLCD(uint num1, uint num2) public view returns (uint){
        return num1 * num2 / GetGCD(num1, num2);
    }
}