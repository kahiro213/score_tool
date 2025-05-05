# score_tool.py

def judge_scores(students):
    for student in students:
        name = student['name']
        score = student['score']
        if score >= 90:
            print(f'{name}さんはSランクです。')
        elif 70 <= score < 90:
            print(f'{name}さんはAランクです。')
        elif 50 <= score < 70:
            print(f'{name}さんはBランクです。')
        else:
            print(f'{name}さんはCランクです。')

def average_score(students):
    total = 0
    for student in students:
        score = student['score']
        total += score
    avg = total / len(students)
    return avg

def save_results(students, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        total = 0
        for student in students:
            name = student['name']
            score = student['score']
            total += score

            if score >= 90:
                rank = "S"
            elif score >= 70:
                rank = "A"
            elif score >= 50:
                rank = "B"
            else:
                rank = "C"

            f.write(f'{name}さんは{rank}ランクです。\n')

        avg = total / len(students)
        f.write(f'\n平均点: {avg:.2f}\n')

def main():
    students = [
        {"name": "田中", "score": 90},
        {"name": "佐藤", "score": 78},
        {"name": "鈴木", "score": 65},
        {"name": "山田", "score": 48}
    ]

    judge_scores(students)
    avg = average_score(students)
    print(f'\nクラスの平均点は{avg:.2f}点です。')

    save_results(students, 'result.txt')
    print(" 結果を result.txt に保存しました！")

if __name__ == '__main__':
    main()
