# specify a pyton module to run to output
# In this we are using base64 module
import base64

# Enter a text to encode
text =  "Hello world"

encode_text = base64.b64encode(text.encode('utf-8'))

# print encoded text
print(encode_text)

# To decode the text we use decode function

decode_text = base64.b64decode(encode_text.decode('utf-8'))

# print decode text or original text
print(decode_text)