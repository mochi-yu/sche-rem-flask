# 8桁のUUIDを生成するためのコードです
import uuid
import random
import string

# 8桁のランダムな文字列を生成する関数
def generate_8_digit_uuid():
    # ランダムな8桁の文字列を生成
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

# 8桁のランダムな文字列を生成
eight_digit_uuid = generate_8_digit_uuid()
print(eight_digit_uuid)
