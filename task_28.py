def encode(str_to_encode):
    encrypt_table = 'abcdefghijklmnopqrstuvwxyz0123456789'
    lower_input = str_to_encode.lower()
    result = ''
    encryption_interval = 5
    for i in range(len(lower_input)):
        position = encrypt_table.find(lower_input[i])
        if position != -1 and encryption_interval + position < len(encrypt_table):
            result += encrypt_table[position + encryption_interval]
        elif encryption_interval + position >= len(encrypt_table):
            result += encrypt_table[(encryption_interval + position) - len(encrypt_table)]
        else:
            result += lower_input[i]
    return result

str_to_encode = input("Please, enter various symbols: ")
print(encode(str_to_encode))
