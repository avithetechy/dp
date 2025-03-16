import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyCDImBhoDS3EB8MQdvPmUyD6vlwPOz0yZ8"

def fetchit():
    try:
        #1 a35
        aurl1 = "https://www.amazon.in/samsung-Awesome-Iceblue-Storage-Without/dp/B0CXMCX9MD/ref=sr_1_2?crid=2K304NFKFTV3R&dib=eyJ2IjoiMSJ9.ljiI4FiiKkM4vYl9peks-xdknRL9kkTLknKbBQLfK1MFWNRH6JK8ztGmS6tRYjsc24vLtViZouC1rMZHxgbknwKPmpx8frU4jxiEzmXIqliWezEUkhZWkO7enZ8nRS97A7dYQeBuMBctJ8OITV8cHeZ3tEg-BiIyMGbv-sRfxPfk8seKwaGJvOY3ZXT7ZtVMrVqcdqo-fAbfg9iodCn9QbKszHWi0hRaCK7cLRHSphk.fMzbdMgC2OftrfCX6Baem6oXbMEz6lMb07R6VtLMfqM&dib_tag=se&keywords=samsung+Galaxy+A35+5G&nsdOptOutParam=true&qid=1740226476&sprefix=samsung+galaxy+a35+5g%2Caps%2C270&sr=8-2"

        text_sys_prompt = f"extract only the product name like Samsung Galaxy A35 5G and its price like 25499 as integer from this url:{aurl1}"

        genai.configure(api_key=GOOGLE_API_KEY)
        #model1 = genai.GenerativeModel(model='gemini-2.0-pro',system_instruction='text_sys_prompt')
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
                #if product_name:
                    #reslst.append(product_name) 
                if price:
                    reslst.append(price) 
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")

        furl1 = "https://www.flipkart.com/samsung-galaxy-a35-5g-awesome-iceblue-128-gb/p/itm9684d2fe9201e?pid=MOBGYT2HEYWFCG8Q&lid=LSTMOBGYT2HEYWFCG8QGSQZ9H&marketplace=FLIPKART&q=samsung%20Galaxy%20A35%205G&sattr[]=color&sattr[]=storage&st=storage"

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
                #if product_name:
                    #reslst.append(product_name)
                if price:
                    reslst.append(price)
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")


        aurl2 = "https://www.amazon.in/Apple-iPhone-15-Pro-512/dp/B0CHX45NRR/ref=sr_1_1_sspa?crid=3PPIC2WAPPS5J&dib=eyJ2IjoiMSJ9.jAYzoAoHiP2F2DOvR9YQ0VejrlRzgpxjNFvn5EeRrud3bTAyHsjnQlRBVombFYdyDE1s2SUuWc2d-l_7gRBCe6kzVPS-F83x4KECr-kUHkReTyXuvR-Y7dPm7hC7QUM9IPSiJGLRSW_D6xVXqu2U9L6O0Jqi8kkCmHZxj1zp6L8lQF7oj2-6vl7YOEjarB2vWhcn_LzIqQCivcVN2fSLQ84JV0wt5rMjg7VlFQHYGoY.aH0L6erxGmYNXax1CfpbP0Q080oJ6Kf8jZCIOXFu1QQ&dib_tag=se&keywords=Apple+iPhone+15+Pro&nsdOptOutParam=true&qid=1740226721&sprefix=apple+iphone+15+pro%2Caps%2C349&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

        text_sys_prompt2 = f"extract only the product name like Apple Iphone 15 pro and its price like 129900 from this url:{aurl2}"

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
                #if product_name:
                    #reslst.append(product_name)
                if price:
                    reslst.append(price)
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")


        furl2 = "https://www.amazon.in/Apple-iPhone-15-Pro-512/dp/B0CHX45NRR/ref=sr_1_1_sspa?crid=3PPIC2WAPPS5J&dib=eyJ2IjoiMSJ9.jAYzoAoHiP2F2DOvR9YQ0VejrlRzgpxjNFvn5EeRrud3bTAyHsjnQlRBVombFYdyDE1s2SUuWc2d-l_7gRBCe6kzVPS-F83x4KECr-kUHkReTyXuvR-Y7dPm7hC7QUM9IPSiJGLRSW_D6xVXqu2U9L6O0Jqi8kkCmHZxj1zp6L8lQF7oj2-6vl7YOEjarB2vWhcn_LzIqQCivcVN2fSLQ84JV0wt5rMjg7VlFQHYGoY.aH0L6erxGmYNXax1CfpbP0Q080oJ6Kf8jZCIOXFu1QQ&dib_tag=se&keywords=Apple+iPhone+15+Pro&nsdOptOutParam=true&qid=1740226721&sprefix=apple+iphone+15+pro%2Caps%2C349&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

        text_sys_prompt2 = f"extract only the product name like Apple Iphone 15 pro and its price like 134900 from this url:{furl2}"

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
                #if product_name:
                    #reslst.append(product_name)
                if price:
                    reslst.append(price)
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")



        aurl3 = "https://www.amazon.in/Samsung-Celestial-MediaTek-Dimensity-Security/dp/B0DGXB4SX1/ref=sr_1_1?crid=1BTUMY8AMMOKO&dib=eyJ2IjoiMSJ9.PO4QK90JuN5C1bQkYLynqEnagSjpd6rwEA_YO_ZYJVFAKm4Br6ivamLlfFRCQG3wdLgk1vBZLIA-Kelea9G7GEIOapO9w2hTLGSDsthJldvWNpJY8ttYqN3qGhZ8a-HBf8IvtelOvKPcyYWk0UNXMKK9kqFA6MmcTl7j0u4qGArLDlnVOjFYEerWBmffIGaP5EY-6rdww4rXSWwO0Wsd0NBJEaeo_ORuqami6rbEKwA.SXZM43Zs1g-29sKdArKYpp7IbKfvmzI164rPxnVJVto&dib_tag=se&keywords=Samsung%2BGalaxy%2BM15%2B5G&nsdOptOutParam=true&qid=1740226842&sprefix=samsung%2Bgalaxy%2Bm15%2B5g%2Caps%2C358&sr=8-1&th=1"

        text_sys_prompt2 = f"extract only the product name like Samsung galaxy m15 5G and its price like 12999 from this url:{aurl3}"

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
                #if product_name:
                    #reslst.append(product_name)
                if price:
                    reslst.append(price)
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")


        furl3 = "https://www.flipkart.com/samsung-galaxy-m15-5g-celestrial-blue-128-gb/p/itmf5a4280beb534?pid=MOBHYNBPZRHB6TKN&lid=LSTMOBHYNBPZRHB6TKN4U4RN2&marketplace=FLIPKART&q=Samsung%20Galaxy%20M15%205G&sattr[]=color&sattr[]=ram&st=color&otracker=search"

        text_sys_prompt2 = f"extract only the product name like Samsung Galaxy m15 5G and its price like 14241 from this url:{furl3}"

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
                #if product_name:
                    #reslst.append(product_name)
                if price:
                    reslst.append(price)
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")



        aurl4 = "https://www.amazon.in/Samsung-Smartphone-Titanium-Whitesilver-Included/dp/B0DSKNQW8F/ref=sr_1_11_sspa?crid=3D6Y7D1NEPKI0&dib=eyJ2IjoiMSJ9.vdxDFClLx4dwbLMsFvEF4dAC892sD-1opSN8c1-i3AqMERM6si_FMpvVDW_4FS7uMHtsQcwDcesVGbrex5JNYdNvv-fqvefp3QBQ6jH3U4lV1lb5CgIPPPfqpe-2owDIRYigz4bCHaigeCQC8JpbPe0rSMTHYV-eazJf0dvuTPJakV6cAshHVidUC9budGl-cb-vVH5YWP1SnIYsTARrj0eCDfeyOYBmwsfxhoJHvmY.Kn6c9pH9rsOnvQo1drjQZaPIJC4OGjGIhftcfixNkWE&dib_tag=se&keywords=google%2Bpixel&nsdOptOutParam=true&qid=1740227528&sprefix=google%2Bpixle%2Caps%2C292&sr=8-11-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&th=1"

        text_sys_prompt2 = f"extract only the product name like Samsung galaxy s25 ultra and its price like 129999 from this url:{aurl4}"

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
                #if product_name:
                    #reslst.append(product_name)
                if price:
                    reslst.append(price)
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")


        furl4 = "https://www.flipkart.com/samsung-galaxy-s25-ultra-5g-titanium-black-256-gb/p/itm09d676ceb930d?pid=MOBH8K8UVNGVNGKN&lid=LSTMOBH8K8UVNGVNGKNFV5MBM&marketplace=FLIPKART&q=s25+ultra&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=854bba3e-576c-4a1d-b41c-4b5517342a49.MOBH8K8UVNGVNGKN.SEARCH&ppt=sp&ppn=sp&ssid=ff4x2wh9ow0000001740227703780&qH=62b6366dfbe5c56b"

        text_sys_prompt2 = f"extract only the product name Samsung Galaxy s25 ultra and its price as 129999 from this url:{furl4}"

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
                #if product_name:
                    #reslst.append(product_name)
                if price:
                    reslst.append(price)
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")


        aurl5 = "https://www.amazon.in/OnePlus-12R-Iron-Gray-Storage/dp/B0CX2L28HH/ref=sr_1_2?crid=2IJDXMTZK86H7&dib=eyJ2IjoiMSJ9.2aZrUPIYefQ5Rvv-9stIFjbbdOULcfZ2UO_Y7dNopECgkaZq28sXD3GO3cC4VhyPg1PPXhE4KKxp9GUj-ZUc7Mc3brD_IxONiAWi4vTtJkVxre6rklJulOpRBsOknSxGiAQqnHPgI0-fkxlBwhCmdQOcdM_-cPbS6OPbb5L05xy0NrKKyl5LPiz7q97OaWukSazqrCYzkUwp3OalZTM948bYXazUepZ-3DrarKzKuQI.kk1wgn6QOUusgrBMcZWeIrKuGcy50XbK0HZ2Tm5lNA0&dib_tag=se&keywords=OnePlus%2B12R&nsdOptOutParam=true&qid=1740227035&sprefix=oneplus%2B12r%2Caps%2C242&sr=8-2&th=1"

        text_sys_prompt2 = f"extract only the product name like OnePlus 12 R and its price like 32999 from this url:{aurl5}"

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
                #if product_name:
                    #reslst.append(product_name)
                if price:
                    reslst.append(price)
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")


        furl5 = "https://www.flipkart.com/oneplus-12r-iron-gray-256-gb/p/itm347349f7db2f2?pid=MOBGZ8RSPHZWR22T&lid=LSTMOBGZ8RSPHZWR22TJ4QNKU&marketplace=FLIPKART&q=OnePlus+12R&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=898d7e72-b3a2-4618-ab02-60dab4ff1fe0.MOBGZ8RSPHZWR22T.SEARCH&ppt=pp&ppn=pp&ssid=dx4icajuww0000001740227030053&qH=fb04ca996d9d7abc"

        text_sys_prompt2 = f"extract only the product name like OnePlus 12 R and its price like 37495 from this url:{furl5}"

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
                #if product_name:
                    #reslst.append(product_name)
                if price:
                    reslst.append(price)
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")


        aurl6 = "https://www.amazon.in/realme-Storage-Prolight-Dimensity-SUPERVOOC/dp/B0C78DSV4H/ref=sr_1_2?crid=3A7R63204HVI0&dib=eyJ2IjoiMSJ9.QmPQA9sN3YnV6AaLWweZHwlSwPJRHgjbZPfUYmoen00UjBN277KTI3QMqsSwRqliXD58B2NEFRmRuVg0cMhX_t60RNMsZHAVKjCZwXtRE9WYMvztclfXh2oIdv4BPR5U6llQsM1OGPg9VYKW8qm7ug1zFMeMvOM_ORn87ANbHyYzgbM1J2gJ-JURYi9TTyVyeW-lLzAxxHgU1t4cqpAiZ5gEo_vFdEoYgo4wH4tG3ZM.FhAJqAw50hIZUtwQgt6cF54yAHqN5sAXJAaYi8dWgRw&dib_tag=se&keywords=Realme+11+Pro%2B+5G&nsdOptOutParam=true&qid=1740227091&sprefix=realme+11+pro%2B+5g%2Caps%2C765&sr=8-2"

        text_sys_prompt2 = f"extract only the product name like Realme 11 Pro+ 5G and its price like 26999 from this url:{aurl6}"

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
                #if product_name:
                    #reslst.append(product_name)
                if price:
                    reslst.append(price)
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")

        furl6 = "https://www.flipkart.com/realme-11-pro-5g-oasis-green-256-gb/p/itm5647cce338e55?pid=MOBGPU8H9KVVVHMS&lid=LSTMOBGPU8H9KVVVHMSM5WQKX&marketplace=FLIPKART&q=Realme+11+Pro%2B+5G&store=tyy%2F4io&srno=s_1_3&otracker=search&otracker1=search&fm=Search&iid=3ffe33c6-d937-465a-9a2a-cc31144db875.MOBGPU8H9KVVVHMS.SEARCH&ppt=pp&ppn=pp&ssid=pghtwkx0vk0000001740227084348&qH=3f99404190bbc483"

        text_sys_prompt2 = f"extract only the product name like Realme 11 Pro+ 5G and its price like 27999 from this url:{furl6}"

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
                #if product_name:
                    #reslst.append(product_name)
                if price:
                    reslst.append(price)
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")


        aurl7 = "https://www.amazon.in/iQOO-Storage-Dimensity-Processor-Segment/dp/B07WGPKNGT/ref=sr_1_1?crid=1GX945OLBP2V0&dib=eyJ2IjoiMSJ9.orwBxm-ErU8yrVwTChN5ty1TD82jjWYmeR52TALFNKStlgK3mCcIaJf33opnUnpK4QN-31VM3ODbQz3jmKPlr74lWIxJHv8HHPRAzlSXRCqOSJsZhAYT_nKubftMq74kMTPFfIsclPSTsV0na4fVjVCdrOEE9CTVTRc9RxWq9lYgNOezNRXtr8UWYW1OYvw1T27gh1pcQ0-FYo1aMQidbbEubDYGWCuMy9ii_TChQt4.XiACVg8r8xie_FMUfqmIEJQbWzCu-A0-TtDh2eyeSy0&dib_tag=se&keywords=iQOO+Neo+7&nsdOptOutParam=true&qid=1740227147&sprefix=iqoo+neo+7%2Caps%2C297&sr=8-1"

        text_sys_prompt2 = f"extract only the product name like iQOO Neo 7 and its price like 29999 from this url:{aurl7}"

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
                #if product_name:
                    #reslst.append(product_name)
                if price:
                    reslst.append(price)
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")

        furl7 = "https://www.flipkart.com/iqoo-neo-7-5g-interstellar-black-256-gb/p/itm58818bb276753?pid=MOBGN9WJTWGNAZHG&lid=LSTMOBGN9WJTWGNAZHGYGUPQ0&marketplace=FLIPKART&q=iQOO+Neo+7&store=tyy%2F4io&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=92ff11e5-7e09-46b0-bab1-0227cecb9573.MOBGN9WJTWGNAZHG.SEARCH&ppt=sp&ppn=sp&ssid=ri2inhr9v40000001740227157627&qH=cccbd3e846103fad"

        text_sys_prompt2 = f"extract only the product name like iQOO Neo 7 and its price like 30829 from this url:{furl7}"

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
                #if product_name:
                    #reslst.append(product_name)
                if price:
                    reslst.append(price)
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")

        aurl8 = "https://www.amazon.in/Redmi-Note-pro-Scarlet-256gb/dp/B0D66RDWT6/ref=sr_1_1?crid=3DW7STCAG4RPI&dib=eyJ2IjoiMSJ9.aeqdNvyIQ74i9fiKjGPXk3CPNuFOjMmpILmjXM-zil3GKyb5O014GOwZD3GC4nryl-Tj3V5AKPu_Rf2HpTysLg3k1u-DFZZBbt0fS8FKeDrqOoZ-oFs1fdxXB6oMKVmg8VcGK8JGK-Lcf4ZT-470_G6dtkdMqQ9rW7vd7xNfBBcZZg4KIlCRqDLFkrz-Uiahbs5YBpuF-7VvHK6y8ZmlWyRH0StiW_EzFjBBGR8Rdos.zkp-LXw_l0ctYtW8vE71aV_eWs2mJred8oLBy84yNHw&dib_tag=se&keywords=Xiaomi+13+Pro&nsdOptOutParam=true&qid=1740227204&sprefix=xiaomi+13+pro%2Caps%2C976&sr=8-1"

        text_sys_prompt2 = f"extract only the product name like Redmi Note 13 pro and its price like 19040 from this url:{aurl8}"

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
                #if product_name:
                    #reslst.append(product_name)
                if price:
                    reslst.append(price)
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")

        furl8 = "https://www.flipkart.com/redmi-note-13-pro-5g-scarlet-red-128-gb/p/itmff04a1b8e153d?pid=MOBH3FK3Q64XBYHZ&lid=LSTMOBH3FK3Q64XBYHZFPJO3W&marketplace=FLIPKART&q=Xiaomi+13+Pro&store=tyy%2F4io&srno=s_1_4&otracker=search&otracker1=search&fm=Search&iid=52987e00-178e-445e-9274-33180861f40d.MOBH3FK3Q64XBYHZ.SEARCH&ppt=pp&ppn=pp&ssid=w049uwit8w0000001740227212943&qH=bce75983da1b7144"

        text_sys_prompt2 = f"extract only the product name like Redmi Note 13 pro and its price like 19800 from this url:{furl8}"

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
                #if product_name:
                    #reslst.append(product_name)
                if price:
                    reslst.append(price)
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")


        aurl9 = "https://www.amazon.in/Vivo-Smartphone-Andaman-256GB-Storage/dp/B0DBQC4345/ref=sr_1_3?crid=1LAR4XUHDSDMB&dib=eyJ2IjoiMSJ9.lZ0WR7Y845N47WEKRrFei7u9wJKlojuE-A5q2diIBU5JuLOo7Fwmw-mT-kDxxdQiY61Xef4GtjSZ55vRhd60pm0wZwRHR9oYxTBFtsfasa_z80FIg32F16BmaTJG1DPXqsiXhxUe010t9a1gkcfq973Rw6ojryR_OU8Ddzui_eNqLWRn3CVEmQoOUaIYPphj4h6W0jZWwn7Dh9yHNAZJW_ptLJDjQOF0SDRtWLmteKM.5QS40f1imuUEHJU5Hdb04_VN74s-7ftLAvZdeNPgeDM&dib_tag=se&keywords=vivo+v30&nsdOptOutParam=true&qid=1740228386&sprefix=vivo+v30%2Caps%2C313&sr=8-3"

        text_sys_prompt2 = f"extract only the product name like vivo v30 pro and its price like 36249 from this url:{aurl9}"

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
                #if product_name:
                    #reslst.append(product_name)
                if price:
                    reslst.append(price)
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")

        furl9 = "https://www.flipkart.com/vivo-v30-pro-5g-andaman-blue-512-gb/p/itmd7b7a1700c431?pid=MOBGYGCBNRTAHBBV&lid=LSTMOBGYGCBNRTAHBBVRAKIUN&marketplace=FLIPKART&q=vivo+v30+pro&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=27c5f4e7-e18d-4c1b-a3cc-68d9da4e2263.MOBGYGCBNRTAHBBV.SEARCH&ppt=sp&ppn=sp&ssid=99t2pl6b4w0000001740228399277&qH=4239a8c3ca17096e"

        text_sys_prompt2 = f"extract only the product name like vivo v30 pro and its price like 39999 from this url:{furl9}"

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
                #if product_name:
                    #reslst.append(product_name)
                if price:
                    reslst.append(price)
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")    

        aurl10 = "https://www.amazon.in/Nothing-Storage-Display-Qualcomm-Snapdragon/dp/B0CBYW7RXB/ref=sr_1_1?crid=1KN41Q26H3HED&dib=eyJ2IjoiMSJ9.2UX2DHIerUpO0GW2dlAETMmlZKaC_LL8dlSYtErFEiZz80hkFGe_YjUZylXwBCT6kzSrNrKt-FY0icCjv6GdQtBrJTQ2ThOj3qoOIsAjEhCZ4_ibsWgQpcvAsJ_RFxZQmoAuY6Xs0MhObusp_v_8duTBwA4MYf66eJQeMvk45OmntyyNMvKz5VroQ1iTijUvfV-gUljxea0V7PFEWviRMsUpN3qu6foHbnzS1aiXlKI.dWBUt1sijHuYjigvkw_ch9GBEDZvw2j2ykm3KIV5Jcc&dib_tag=se&keywords=Nothing%2BPhone%2B(2)&qid=1740227352&sprefix=vivo%2Bv29%2Bpro%2Caps%2C261&sr=8-1&th=1"

        text_sys_prompt2 = f"extract only the product name like Nothing Phone 2 and its price like 39800 from this url:{aurl10}"

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
                #if product_name:
                    #reslst.append(product_name)
                if price:
                    reslst.append(price)
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")

        furl10 = "https://www.flipkart.com/nothing-phone-2-white-512-gb/p/itmc1490711c3eb9?pid=MOBGZSDKJYHHV3KN&lid=LSTMOBGZSDKJYHHV3KNEMJPQM&marketplace=FLIPKART&q=Nothing+Phone+%282%29&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=5d3e7d35-f1dc-492d-bf2a-bf5bf20d2bea.MOBGZSDKJYHHV3KN.SEARCH&ppt=pp&ppn=pp&ssid=oq8ff20bb40000001740227344962&qH=69406e08873eece2"

        text_sys_prompt2 = f"extract only the product name like Nothing Phone 2 and its price like 39999 from this url:{furl10}"

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
                #if product_name:
                    #reslst.append(product_name)
                if price:
                    reslst.append(price)
            else:
                print("No content or parts found in the response.")

        else:
            print("No candidates found in the response.")
        return reslst
    
    except:
        reslst = ['23995','25544','129900','134900','12999','14241','129999','129999','32999','37495','27000','27999','30500','30829','19040','19800','36249','39999','39800','39999']
        return reslst


