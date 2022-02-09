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
# properties Information

# Database of properties including their name, digital address, detail and  cost per Ether.
# A single Ether is currently valued at $3000
properties_database = {
    "Montauk Surfside": ["Montauk Surfside", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "66 Surfside Ave, Montauk, NY 11954", 6333, "Images/Montauk.jpg"],
    "The Baldhead House": ["The Baldhead House", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "218 Station House Way, Bald Head Island, NC 28461", 1990, "Images/Baldhead.jpg"],
    "Cliff House": ["Cliff House", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "62 Sols Cliff Rd, Bar Harbor, ME 04609", 2970, "Images/Cliff.jpg"],
    "The Delaware Farm": ["The Delaware Farm", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "23556 Sloan Rd, Harbeson, DE 19951",1585, "Images/Delaware.jpg"]
 
}

# A list of the properties
properties = ["Montauk Surfside", "The Baldhead House", "Cliff House", "The Delaware Farm"]


def get_properties():
    """Display the database of properties information."""
    db_list = list(properties_database.values())

    for number in range(len(properties)):
        st.image(db_list[number][4], width=400)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum  Address: ", db_list[number][1])
        st.write("Property Address: ", db_list[number][2])
        st.write("Ethereum Price : ", db_list[number][3], "eth")
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
#st.sidebar.write(get_balance)

##########################################

# Create a select box to chose a property
properties = st.sidebar.selectbox('Select a property', properties)

# Create a input field to record the number of Shares the properties worked
Shares = st.sidebar.number_input("Quantity  of Shares")

st.sidebar.markdown("## Estate Name, Quantity of Shares, and Ethereum Address")

# Identify the property
properties = properties_database[properties][0]

# Write the property   name to the sidebar
st.sidebar.write(properties)

# Identify the property  fractional share
fractional_share = properties_database[properties][3]

# Write the inTech Finder properties' fractional share to the sidebar
st.sidebar.write(fractional_share)

# Identify the property Ethereum Address
properties_address = properties_database[properties][1]

# Write the property Ethereum Address to the sidebar
st.sidebar.write(properties_address)

# Write the property name to the sidebar

st.sidebar.markdown("## Total Cost in Ether")

################################################################################


##########################################

# Calculate total `Cost` for the properties by multiplying the property fractional shares
# rate from the property database (`properties_database[properties][3]`) by the
# value of the `Shares` variable
Cost  = fractional_share*Shares


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
# Writes properties propertiess to the Streamlit page
get_properties()