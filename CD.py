#build a cryptocurrency dashboard

#import libraries
from matplotlib.pyplot import get
from pandas.core.frame import DataFrame
import streamlit as st 
import pandas as pd
import datetime
import plotly.graph_objects as go
from PIL import Image 



# streamlit run "C:\Users\nagas\Desktop\CRYPTODASH\CD.py"
st.write("""# **CRYPTOCURRENCY DASHBOARD**
             analyzes the crypto currencies  """)
#image==Image.open(r"C:/Users/nagas/PycharmProjects/CRYPTODASH/cryptocurrency.jpeg")
#st.image(image, use_column_width=True)
#image.show()

st.sidebar.header("User Input")

def get_input(): 
    start_date=st.sidebar.text_input("Start date")
    end_date = st.sidebar.text_input("End date",)
    crypto_symbol = st.sidebar.text_input("Crypto Symbol")
    return start_date,end_date,crypto_symbol


def get_name(crypto_symbol):
    if crypto_symbol=="BTC":
        return "Bitcoin"
    elif crypto_symbol == "ETH" :
        return "Ethereum"
    elif crypto_symbol == "DOGE" :
        return "Dogecoin"
    else:
        return "None"

def get_data(start,end,symbol):
    symbol=symbol.upper()
    if symbol=="BTC":
        data=pd.read_csv("C:/Users/nagas/PycharmProjects/CRYPTODASH/coin_Bitcoin.csv")
        df=DataFrame(data)
        return df
    elif symbol=="ETH":
        data=pd.read_csv("C:/Users/nagas/PycharmProjects/CRYPTODASH/coin_Ethereum.csv")
        df=DataFrame(data)
        return df
    elif symbol == "DOGE":
        data = pd.read_csv("C:/Users/nagas/PycharmProjects/CRYPTODASH/coin_Dogecoin.csv")
        df=DataFrame(data)
        return df
    else:
        df=pd.DataFrame(Columns= data['Date ','High','Low','Open ','Close','Volume','market cap'])
        return df

    start=pd.to_datetime(start)
    end = pd.to_datetime(end)
    df=df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.rev[end:start]





start,end,symbol=get_input()
get_data(start,end,symbol)
name=get_name(symbol)

df=get_data(start,end,symbol)

fig=go.Figure(
    data=(go.Candlestick(
        x=df.index ,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        increasing_line_color='green',
        decreasing_line_color='red'
    )
)
)
st.header("Data")
st.write(df)

st.header(" Data Statistics")
st.write(df.describe())

st.header(" Close price")
st.line_chart(df['Close'])

st.header(" Volume")
st.bar_chart(df['Volume'])

st.header(" Candle Stick")
st.plotly_chart(fig)