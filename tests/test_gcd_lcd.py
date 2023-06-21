import pytest
from brownie import accounts, GCD_LCD
from brownie.network import priority_fee

@pytest.fixture
def gcd_lcd_contract():
    priority_fee("0.1 gwei")
    return GCD_LCD.deploy({ 'from': accounts[0] })

def test_gcd(gcd_lcd_contract):
    assert gcd_lcd_contract.GetGCD(2, 3) == 1
    assert gcd_lcd_contract.GetGCD(4, 8) == 4
    assert gcd_lcd_contract.GetGCD(9, 126) == 9
    assert gcd_lcd_contract.GetGCD(1000, 205) == 5

def test_lcd(gcd_lcd_contract):
    assert gcd_lcd_contract.GetLCD(2, 3) == 6
    assert gcd_lcd_contract.GetLCD(10, 100) == 100
    assert gcd_lcd_contract.GetLCD(20, 33) == 660
    assert gcd_lcd_contract.GetLCD(23, 31) == 713
