import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
from accessmlmodel import main
#from productsearch import reslst
import os
from PIL import Image
import io
from prosres import nextlst
# Simulating API response for product prices
def fetch_prices():
    image_dir = "D:/Avinash/projects/dynamicpricing/images/"
    data = [
        {"name": "Samsung Galaxy A35 5G", "image": os.path.join(image_dir,"sa35.jpg" ), "desc": "6.5-inch FHD+, Exynos 1380, 5000mAh", "amazon_price": int(nextlst[0]), "flipkart_price": int(nextlst[1])},
        {"name": "Apple iPhone 15 Pro", "image": os.path.join(image_dir,"aipr.jpg" ), "desc": "6.1-inch Super Retina XDR, A17 Pro, 3274mAh", "amazon_price": int(nextlst[2]), "flipkart_price": int(nextlst[3])},
        {"name": "Samsung Galaxy M15 5G", "image": os.path.join(image_dir,"sm15.jpg" ), "desc": "6.6-inch PLS LCD, MediaTek Dimensity 6100+, 6000mAh", "amazon_price": int(nextlst[4]), "flipkart_price": int(nextlst[5])},
        {"name": "Google Pixel 8", "image": os.path.join(image_dir,"gp8.jpg" ), "desc": "6.2-inch OLED, Google Tensor G3, 4575mAh", "amazon_price": int(nextlst[6]), "flipkart_price": int(nextlst[7])},
        {"name": "OnePlus 12R", "image": os.path.join(image_dir,"op12r.jpg" ), "desc": "6.7-inch AMOLED, Snapdragon 8 Gen 2, 5500mAh", "amazon_price": int(nextlst[8]), "flipkart_price": int(nextlst[9])},
        {"name": "Realme 11 Pro+ 5G", "image": os.path.join(image_dir,"r11p.jpg" ), "desc": "6.7-inch AMOLED, Dimensity 7050, 5000mAh", "amazon_price": int(nextlst[10]), "flipkart_price": int(nextlst[11])},
        {"name": "iQOO Neo 7", "image": os.path.join(image_dir,"iqn7.jpg" ), "desc": "6.78-inch AMOLED, Dimensity 8200, 5000mAh", "amazon_price": int(nextlst[12]), "flipkart_price": int(nextlst[13])},
        {"name": "Xiaomi 13 Pro", "image": os.path.join(image_dir,"x13p.jpg" ), "desc": "6.73-inch LTPO AMOLED, Snapdragon 8 Gen 2, 4820mAh", "amazon_price": int(nextlst[14]), "flipkart_price": int(nextlst[15])},
        {"name": "Vivo V29 Pro", "image": os.path.join(image_dir,"v29p.jpg" ), "desc": "6.78-inch AMOLED, Dimensity 8200, 4600mAh", "amazon_price": int(nextlst[16]), "flipkart_price": int(nextlst[17])},
        {"name": "Nothing Phone (2)", "image": os.path.join(image_dir,"np2a.jpg" ), "desc": "6.7-inch LTPO OLED, Snapdragon 8+ Gen 1, 4700mAh", "amazon_price": int(nextlst[18]), "flipkart_price": int(nextlst[19])}
    ]
    return data

# Fetch product data
product_data = fetch_prices()
df = pd.DataFrame(product_data)
#df['lowest_price'] = df[['amazon_price', 'flipkart_price']].min(axis=1)
df['app_price'] = main()

# Streamlit UI
st.title("📱 Our E-comm mobiles App")
st.write("Compare prices of the latest smartphones from Amazon, Flipkart, and our platform.")

# Display products in a grid layout
cnt = 0
cols = st.columns(2)  # Create two columns
for index, row in df.iterrows():
    col = cols[index % 2]
    with col:
        try:
            img = Image.open(row['image'])
            img_bytes = io.BytesIO()
            img.save(img_bytes, format='JPEG')
            st.image(img_bytes, caption=row['name'], width=150)
        except Exception as e:
            st.write(f"Error loading image for {row['name']}: {e}")
        #st.image(row['image'], width=1500)
        st.subheader(row['name'])
        st.write(f"**Description:** {row['desc']}")
        st.write(f"📌 **Amazon Price:** ₹{row['amazon_price']}")
        st.write(f"📌 **Flipkart Price:** ₹{row['flipkart_price']}")
        st.write(f"📌 **Our Price:** ₹{row['app_price']}")
        st.markdown("---")
    cnt+=1
# Price comparison histogram
st.subheader("📊 Price Comparison Histogram")
x = np.arange(len(df))  # Label locations
width = 0.2  # Bar width
fig, ax = plt.subplots()
ax.bar(x - width, df['amazon_price'], width, label='Amazon', color='blue')
ax.bar(x, df['flipkart_price'], width, label='Flipkart', color='orange')
ax.bar(x + width, df['app_price'], width, label='Our Price', color='green')
ax.set_xticks(x)
ax.set_xticklabels(df['name'], rotation=45, ha='right', fontsize=8)
ax.set_ylabel("Prices (₹)")
ax.legend()
st.pyplot(fig)

