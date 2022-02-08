# Cryptocurrency Wallet

################################################################################

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
###############################################################################


################################################################################

# From `crypto_wallet.py import the functions generate_account, get_balance,
#  and send_transaction

from crypto_wallet import generate_account, get_balance, send_transaction



################################################################################
# Exlusive properties properties Information

# Database of Exlusive properties including their name, digital address, detail and  cost per Ether.
# A single Ether is currently valued at $1,500
properties_database = {
    "Lane": ["Lane", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", .20, "Images/lane.jpeg"],
    "Ash": ["Ash", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", .33, "Images/ash.jpeg"],
    "Jo": ["Jo", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "Images/jo.jpeg"],
    "Kendall": ["Kendall", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "Images/kendall.jpeg"]
}

# A list of the Exlusive properties propertiess first names
properties = ["Lane", "Ash", "Jo", "Kendall"]


def get_properties():
    """Display the database of properties information."""
    db_list = list(properties_database.values())

    for number in range(len(properties)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Property Address: ", db_list[number][1])
        st.write("Property Rating: ", db_list[number][2])
        st.write("Cost per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Property Listings")
st.markdown("## Available Investments ")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################

#  Call the `generate_account` function and save it as the variable `account`
account = generate_account(w3)

##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

##########################################

# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar
st.sidebar.write(get_balance)

##########################################

# Create a select box to chose a FinTech Hire properties
properties = st.sidebar.selectbox('Select a properties', properties)

# Create a input field to record the number of Shares the properties worked
Shares = st.sidebar.number_input("Quantity  of Shares")

st.sidebar.markdown("## properties Name, quantity of Shares, and Ethereum Address")

# Identify the FinTech Hire properties
properties = properties_database[properties][0]

# Write the Exlusive properties properties's name to the sidebar
st.sidebar.write(properties)

# Identify the Exlusive properties properties's hourly rate
shares_qty = properties_database[properties][3]

# Write the inTech Finder properties's hourly rate to the sidebar
st.sidebar.write(shares_qty)

# Identify the Exlusive properties properties's Ethereum Address
properties_address = properties_database[properties][1]

# Write the inTech Finder properties's Ethereum Address to the sidebar
st.sidebar.write(properties_address)

# Write the Exlusive properties properties's name to the sidebar

st.sidebar.markdown("## Total Cost in Ether")

################################################################################


##########################################

# Calculate total `Cost` for the properties by multiplying the properties’s hourly
# rate from the properties database (`properties_database[properties][3]`) by the
# value of the `Shares` variable
Cost  = shares_qty*Shares


# Write the `Cost` calculation to the Streamlit sidebar
st.sidebar.write(Cost)

##########################################

# * Save the transaction hash that the `send_transaction` function returns as a
# variable named `transaction_hash`, and have it display on the application’s
# web interface.


if st.sidebar.button("Make Payment"):

    
    # Call the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `properties_address`, and the `Cost` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    transaction_hash = send_transaction(w3,account, properties_address, Cost)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes Exlusive properties propertiess to the Streamlit page
get_properties()