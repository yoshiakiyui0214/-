import random

def main():
    secret = random.randint(1, 100)
    attempts = 0

    print("=== 数当てゲーム ===")
    print("1〜100の整数を当ててください！")
    print()

    while True:
        try:
            guess = int(input("あなたの予想: "))
        except ValueError:
            print("整数を入力してください。\n")
            continue

        if guess < 1 or guess > 100:
            print("1〜100の範囲で入力してください。\n")
            continue

        attempts += 1

        if guess < secret:
            print("もっと大きい数です。\n")
        elif guess > secret:
            print("もっと小さい数です。\n")
        else:
            print(f"正解！ {secret} です！")
            print(f"挑戦回数: {attempts} 回")
            break

if __name__ == "__main__":
    main()
