# Decentralized REIT

################################################################################

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
import json
###############################################################################


################################################################################

# From `crypto_wallet.py import the functions generate_account, get_balance,
#  and send_transaction

from crypto_wallet import generate_account, get_balance, send_transaction



################################################################################
# Exlusive properties properties Information

# Database of Exlusive properties including their name, property address, cost per Ether, and links to photos.
# A single Ether is currently valued at $3,000
properties_database = {
    "Montauk Surfside": ["Montauk Surfside", "66 Surfside Ave, Montauk, NY 11954", 6333, "https://www.zillow.com/homedetails/66-Surfside-Ave-Montauk-NY-11954/32656237_zpid/?mmlb=g,0", "https://www.zillow.com/homedetails/66-Surfside-Ave-Montauk-NY-11954/32656237_zpid/?mmlb=g,1", "https://www.zillow.com/homedetails/66-Surfside-Ave-Montauk-NY-11954/32656237_zpid/?mmlb=g,2", "https://www.zillow.com/homedetails/66-Surfside-Ave-Montauk-NY-11954/32656237_zpid/?mmlb=g,25", "https://www.zillow.com/homedetails/66-Surfside-Ave-Montauk-NY-11954/32656237_zpid/?mmlb=g,28"],
    
    
    "The Baldhead House": ["The Baldhead House", "218 Station House Way, Bald Head Island, NC 28461", 1990, "https://www.zillow.com/homedetails/218-Station-House-Way-Bald-Head-Island-NC-28461/110511869_zpid/?mmlb=g,0", "https://www.zillow.com/homedetails/218-Station-House-Way-Bald-Head-Island-NC-28461/110511869_zpid/?mmlb=g,3", "https://www.zillow.com/homedetails/218-Station-House-Way-Bald-Head-Island-NC-28461/110511869_zpid/?mmlb=g,63", "https://www.zillow.com/homedetails/218-Station-House-Way-Bald-Head-Island-NC-28461/110511869_zpid/?mmlb=g,73", "https://www.zillow.com/homedetails/218-Station-House-Way-Bald-Head-Island-NC-28461/110511869_zpid/?mmlb=g,70"],
    
    "Cliff House": ["Cliff House", "62 Sols Cliff Rd, Bar Harbor, ME 04609", 2970, "https://www.zillow.com/homedetails/62-Sols-Cliff-Rd-Bar-Harbor-ME-04609/217987773_zpid/?mmlb=g,2", "https://www.zillow.com/homedetails/62-Sols-Cliff-Rd-Bar-Harbor-ME-04609/217987773_zpid/?mmlb=g,4", "https://www.zillow.com/homedetails/62-Sols-Cliff-Rd-Bar-Harbor-ME-04609/217987773_zpid/?mmlb=g,6", "https://www.zillow.com/homedetails/62-Sols-Cliff-Rd-Bar-Harbor-ME-04609/217987773_zpid/?mmlb=g,10", "https://www.zillow.com/homedetails/62-Sols-Cliff-Rd-Bar-Harbor-ME-04609/217987773_zpid/?mmlb=g,77"],
    
    "The Delaware Farm": ["The Delaware Farm", "23556 Sloan Rd, Harbeson, DE 19951", 1585, "https://www.zillow.com/homedetails/23556-Sloan-Rd-Harbeson-DE-19951/311545086_zpid/?mmlb=g,135", "https://www.zillow.com/homedetails/23556-Sloan-Rd-Harbeson-DE-19951/311545086_zpid/?mmlb=g,140", "https://www.zillow.com/homedetails/23556-Sloan-Rd-Harbeson-DE-19951/311545086_zpid/?mmlb=g,2", "https://www.zillow.com/homedetails/23556-Sloan-Rd-Harbeson-DE-19951/311545086_zpid/?mmlb=g,5", "https://www.zillow.com/homedetails/23556-Sloan-Rd-Harbeson-DE-19951/311545086_zpid/?mmlb=g,11"]
 
    "Castello Della Balena (Castle of the Whale)": ["Castello Della Balena (Castle of the Whale", "710 Shoals Watch Way, Southport, NC 28461", 2035, "https://www.zillow.com/homedetails/710-Shoals-Watch-Way-Southport-NC-28461/2077753585_zpid/?mmlb=g,0", "https://www.zillow.com/homedetails/710-Shoals-Watch-Way-Southport-NC-28461/2077753585_zpid/?mmlb=g,9", "https://www.zillow.com/homedetails/710-Shoals-Watch-Way-Southport-NC-28461/2077753585_zpid/?mmlb=g,21", "https://www.zillow.com/homedetails/710-Shoals-Watch-Way-Southport-NC-28461/2077753585_zpid/?mmlb=g,22", "https://www.zillow.com/homedetails/710-Shoals-Watch-Way-Southport-NC-28461/2077753585_zpid/?mmlb=g,30"]
}

# A list of the Exlusive properties propertiess first names
properties = ["Montauk Surfside", "The Baldhead House", "Cliff House", "The Delaware Farm", "Castello Della Balena (Castle of the Whale)"]


def get_properties():
    """Display the database of Exlusive propertiess properties information."""
    db_list = list(properties_database.values())

    for number in range(len(properties)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Property Address: ", db_list[number][1])
        st.write("Ethereum Price: ", db_list[number][2], "eth")
        st.write("Photo 1 Link: ", db_list[number][3])
        st.write("Photo 2 Link: ", db_list[number][4])
        st.write("Photo 4 Link: ", db_list[number][5])
        st.write("Photo 4 Link: ", db_list[number][6])
        st.write("Photo 5 Link: ", db_list[number][7])
        st.text(" \n")

################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Exlusive properties!")
st.markdown("## Purchase your special home!")
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