import random

def main():
    secret = random.randint(1, 100)
    attempts = 0

    print("数字当てゲーム！")
    print("1～100の間の数字を当ててください。")

    while True:
        try:
            guess = int(input("あなたの予想: "))
        except ValueError:
            print("整数を入力してください。")
            continue

        if guess < 1 or guess > 100:
            print("1～100の範囲で入力してください。")
            continue

        attempts += 1

        if guess < secret:
            print("もっと大きい数字です。")
        elif guess > secret:
            print("もっと小さい数字です。")
        else:
            print(f"正解！ {attempts}回で当てました！")
            break

if __name__ == "__main__":
    main()
