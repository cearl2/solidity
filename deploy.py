import json
from solcx import compile_standard, install_solc

with open("SimpleStorage.sol", "r", encoding="ascii") as file:
    SimpleStorage_file = file.read()

install_solc("0.6.0")

# compile solidity

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": SimpleStorage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)
# get bytecode
"""
bytecode = compiled_sol["contracts"]["simple_storage.sol"]["simple_storage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = compiled_sol["contracts"]["simple_storage.sol"]["simple_storage"]["abi"]
"""

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)
