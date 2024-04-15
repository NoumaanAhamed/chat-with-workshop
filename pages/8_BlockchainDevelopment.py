# blockchain_web3_page.py

import streamlit as st

def show_blockchain_web3_page():
    st.set_page_config(
        page_title="Blockchain/Web3",
        page_icon="⛓️"
    )

    st.write("# Blockchain/Web3! ⛓️")

    st.sidebar.header("Blockchain/Web3")

    st.markdown(
        """
### Resources:

- [Ethereum Course](https://updraft.cyfrin.io)
- [Web3 Roadmap](https://roadmap.sh/blockchain)
- [Youtube Tutorials](https://www.youtube.com/@PatrickAlphaC)

### Key Topics:

- **Fundamentals**: Blockchain, Solidity/Vyper (Ethereum)
- **Technologies**: Web3.js, Ethers.js, Hardhat, Foundry
- **Explore**: DeFi, DApps, Smart Contracts

### Tips for Blockchain/Web3:

- First, Have an idea of Web2.
- Learn about Blockchain Fundamentals.
- Learn Solidity/Vyper for Ethereum.
- Connet Frontend with Blockchain using Web3.js/Ethers.js.
- Learn about Layer 2 solutions.
- Explore other Blockchains like Solana, Binance Smart Chain, Polkadot.

    """
    )

if __name__ == "__main__":
    show_blockchain_web3_page()
