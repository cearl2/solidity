from solcx import compile_standard, install_solc

with open("simple_storage.sol", "r") as file:
    simple_storage_file = file.read
    print(simple_storage_file)
install_solc("0.6.0")

# compile solidity

complied_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"simple_storage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)
print(complied_sol)
