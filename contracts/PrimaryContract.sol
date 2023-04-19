import "./ERC20.sol";

contract PrimaryContract is ERC20 {
    struct S {
        uint x;
        uint y;
    }

    enum E { READER, WRITER }

    function getX(S calldata s) external returns(uint) {
        return s.x;
    }

    function getAnS() external returns(S memory) {
        return S(0,0);
    }
}

