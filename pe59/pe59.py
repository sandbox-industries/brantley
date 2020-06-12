import time

with open('p059_cipher.txt', 'r') as file:
    hidden_message = list(map(int, file.read().split(',')))


common_eng_words = ['the', 'of', 'and', 'to', 'at', 'be', 'this', 'have', 'from']
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def decrypt_message(key, encrypted_message):
    decrypted_message = []
    for idx in range(0, len(encrypted_message) - 1, 3):

        key_applied = [(encrypted_message[idx] ^ ord(key[0])),
                       (encrypted_message[idx + 1] ^ ord(key[1])),
                       (encrypted_message[idx + 2] ^ ord(key[2]))]

        if False in list(map(is_valid, key_applied)):
            return False

        decrypted_message.extend(list(map(chr, key_applied)))

    return decrypted_message


def is_valid(ascii_code):
    if 31 < ascii_code < 126:
        return True
    else:
        return False


def word_count(word, message_string):
    idx = 0
    counter = 0
    while idx != -1:
        idx = message_string.find(word, idx)
        if idx > -1:
            counter += 1
            idx += len(word)
    return counter


start = time.time()

max_message = ''
max_num_words = 0
correct_key = ''

for a1 in alphabet:
    for a2 in alphabet:
        for a3 in alphabet:
            curr_key = [a1, a2, a3]

            valid_message = decrypt_message(curr_key, hidden_message)

            if valid_message:
                num_words = 0
                valid_message = ''.join(valid_message)

                for common_word in common_eng_words:
                    num_words += word_count(common_word, valid_message)

                if num_words > max_num_words:
                    max_message = valid_message
                    max_num_words = num_words
                    correct_key = curr_key

# answer
print('Key Used: ' + '-'.join(correct_key))
print('Answer:', sum(list(map(ord, max_message))))
print('Run Time:', time.time() - start)








