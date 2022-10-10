from brownie import accounts, config, RSACertification, network


def get_account(walletPassword):
    if network.show_active() == "development":
        # account provided by Ganache-cli
        return accounts[0]
    else:
        # return accounts.add(config["wallets"]["from_key"])
        return accounts.add(walletPassword)
