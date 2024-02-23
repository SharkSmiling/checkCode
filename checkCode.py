import random
import time

def generate_verification_code():
    """生成隨機4碼英文小寫字母的驗證碼"""
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(4))

def main():
    try:
        num_of_questions = int(input("請輸入題數："))
        print("-----------------")
    except ValueError:
        print("請輸入有效的數字。")
        print("-----------------")
        return

    correct_count = 0
    times_per_question = []  # 用來存儲每題的花費時間

    for _ in range(num_of_questions):
        verification_code = generate_verification_code()
        print("驗證碼:", verification_code)

        start_time = time.time()  # 記錄起始時間

        user_input = input("請輸入驗證碼，然後按確定：").strip()

        end_time = time.time()  # 記錄結束時間
        elapsed_time = end_time - start_time  # 計算花費的時間
        times_per_question.append(elapsed_time)  # 將花費時間加入列表

        if user_input == verification_code:
            print(f"正確！花費時間: {elapsed_time:.2f}秒")
            print("-----------------")
            correct_count += 1
        else:
            print("錯誤。正確答案是:", verification_code)
            print("-----------------")

    print(f"總共{num_of_questions}題，你答對了{correct_count}題。")

    # 顯示每一題的花費時間
    for i, time_per_question in enumerate(times_per_question, start=1):
        print(f"第{i}題花費時間: {time_per_question:.2f}秒")

    input("按 Enter 鍵結束程式。")

if __name__ == "__main__":
    main()