import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyCDImBhoDS3EB8MQdvPmUyD6vlwPOz0yZ8"

#1 a35
aurl1 = "https://www.amazon.in/samsung-Awesome-Iceblue-Storage-Without/dp/B0CXMCX9MD/ref=sr_1_2?crid=2K304NFKFTV3R&dib=eyJ2IjoiMSJ9.ljiI4FiiKkM4vYl9peks-xdknRL9kkTLknKbBQLfK1MFWNRH6JK8ztGmS6tRYjsc24vLtViZouC1rMZHxgbknwKPmpx8frU4jxiEzmXIqliWezEUkhZWkO7enZ8nRS97A7dYQeBuMBctJ8OITV8cHeZ3tEg-BiIyMGbv-sRfxPfk8seKwaGJvOY3ZXT7ZtVMrVqcdqo-fAbfg9iodCn9QbKszHWi0hRaCK7cLRHSphk.fMzbdMgC2OftrfCX6Baem6oXbMEz6lMb07R6VtLMfqM&dib_tag=se&keywords=samsung+Galaxy+A35+5G&nsdOptOutParam=true&qid=1740226476&sprefix=samsung+galaxy+a35+5g%2Caps%2C270&sr=8-2"

text_sys_prompt = f"extract only the product name like Samsung Galaxy A35 5G and its price like 25499 from this url:{aurl1}"

genai.configure(api_key=GOOGLE_API_KEY)
#model1 = genai.GenerativeModel(model='gemini-1.5-pro',system_instruction='text_sys_prompt')
model2 = genai.GenerativeModel('gemini-2.0-flash')
response = model2.generate_content(text_sys_prompt)
reslst = []
if response.candidates:  # Check if there are any candidates
    first_candidate = response.candidates[0] # Get the first candidate
    if first_candidate.content and first_candidate.content.parts: #Check if content and parts exist
        text_output = first_candidate.content.parts[0].text

        # Now, extract name and price from the text output
        lines = text_output.strip().split('\n') #Splitting the output into lines
        product_name = None
        price = None
        for line in lines:
            #if "Product Name:" in line:
                #product_name = line.split("Product Name:")[1][3:].strip()
            if "Price:" in line:
                price = line.split("Price:")[1][3:].strip()
        if product_name:
            reslst.append(product_name) 
        if price:
            reslst.append(price) 
    else:
        print("No content or parts found in the response.")

else:
    print("No candidates found in the response.")

furl1 = "https://www.flipkart.com/samsung-galaxy-a35-5g-awesome-iceblue-256-gb/p/itm9684d2fe9201e?pid=MOBGYT2HYAAHS3ZR&lid=LSTMOBGYT2HYAAHS3ZR42NYKW&marketplace=FLIPKART&q=samsung%20Galaxy%20A35%205G&sattr[]=color&sattr[]=storage&st=color"

text_sys_prompt2 = f"extract only the product name like Samsung Galaxy A35 5G and its price like 28999 from this url:{furl1}"

#genai.configure(api_key=GOOGLE_API_KEY)
#model1 = genai.GenerativeModel(model='gemini-1.5-pro',system_instruction='text_sys_prompt')
#model2 = genai.GenerativeModel('gemini-1.5-flash')
response2 = model2.generate_content(text_sys_prompt2)

if response2.candidates:  # Check if there are any candidates
    first_candidate = response2.candidates[0] # Get the first candidate
    if first_candidate.content and first_candidate.content.parts: #Check if content and parts exist
        text_output = first_candidate.content.parts[0].text

        # Now, extract name and price from the text output
        lines = text_output.strip().split('\n') #Splitting the output into lines
        product_name = None
        price = None
        for line in lines:
            #if "Product Name:" in line:
                #product_name = line.split("Product Name:")[1][3:].strip()
            if "Price:" in line:
                price = line.split("Price:")[1][3:].strip()
        if product_name:
            reslst.append(product_name)
        if price:
            reslst.append(price)
    else:
        print("No content or parts found in the response.")

else:
    print("No candidates found in the response.")




print(reslst)