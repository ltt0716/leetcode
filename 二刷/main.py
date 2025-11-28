import json
import random
import os

DB_FILE = "leetcode_problems.json"


def load_data():
    """从JSON文件加载题库数据"""
    if not os.path.exists(DB_FILE):
        print(f"错误: 题库文件 '{DB_FILE}' 不存在！")
        return None
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_data(data):
    """将更新后的数据保存回JSON文件"""
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_all_problems(data):
    """获取所有题目的列表"""
    all_problems = []
    for category, problems in data.items():
        for problem in problems:
            problem['category'] = category  # 给每个题目加上分类信息
            all_problems.append(problem)
    return all_problems


def get_undone_problems(data):
    """获取所有未完成的题目列表"""
    return [p for p in get_all_problems(data) if p['status'] == 'undone']


def mark_as_done(data, problem_id):
    """根据ID标记题目为已完成"""
    found = False
    for category, problems in data.items():
        for problem in problems:
            if problem['id'] == problem_id:
                problem['status'] = 'done'
                found = True
                break
        if found:
            break
    if found:
        save_data(data)
        print(f"\n🎉 恭喜！已将题目 ID:{problem_id} 标记为完成！")
    else:
        print(f"\n❌ 错误: 未找到题目 ID:{problem_id}。")


def show_status(data):
    """显示当前的刷题状态"""
    all_problems = get_all_problems(data)
    done_count = len(all_problems) - len(get_undone_problems(data))
    total_count = len(all_problems)
    progress = (done_count / total_count) * 100 if total_count > 0 else 0

    # print("\n" + "=" * 30)
    print("      📊 当前刷题进度 📊")
    print(f"    已完成: {done_count} / {total_count} 道")
    # print(f"    进度: {progress:.2f}%")
    print("=" * 30 + "\n")


def get_leetcode_url(problem_id, title):
    """生成力扣题目链接"""
    # 将中文标题转换为URL格式 (简单替换)
    slug = title.lower().replace(' ', '-')
    return f"https://leetcode.cn/problems/{slug}/"


def main():
    """主程序循环"""
    data = load_data()
    if not data:
        return

    print("🚀 欢迎来到 LeetCode 刷题助手! 🚀")

    while True:
        show_status(data)

        command = input("👉 请输入命令 (next, done, list, quit): ").strip().lower()

        if command == "next":
            undone_problems = get_undone_problems(data)
            if not undone_problems:
                print("\n🎉🎉🎉 恭喜你！所有题目都已完成！🎉🎉🎉")
                continue

            problem = random.choice(undone_problems)
            print("\n" + "*" * 40)
            print("        🔥为你随机抽取一道题🔥")
            print(f"  分类: {problem['category']}")
            print(f"  ID:   {problem['id']}")
            print(f"  题目: {problem['title']}")
            print(f"  难度: {problem['difficulty']}")
            # print(f"  链接: {get_leetcode_url(problem['id'], problem['title'])}")
            # print("*" * 40 + "\n")

        elif command.startswith("done"):
            try:
                # 支持 "done 1" 或 "done1" 这种格式
                parts = command.split()
                if len(parts) > 1:
                    problem_id = int(parts[1])
                else:
                    problem_id = int(command[4:])  # "done" 后面就是id
                mark_as_done(data, problem_id)
            except (ValueError, IndexError):
                print("\n❌ 格式错误! 请输入 'done <题目ID>', 例如: 'done 49'")

        elif command == "list":
            print("\n" + "-" * 40)
            print("           📋 题目完成状态列表 📋")
            for category, problems in data.items():
                print(f"\n--- {category} ---")
                for p in problems:
                    status_icon = "✅" if p['status'] == 'done' else "❌"
                    print(f"  {status_icon} ID:{p['id']:<4} {p['title']}")
            print("-" * 40 + "\n")

        elif command == "quit":
            print("\n👋 坚持就是胜利，下次再见！")
            break

        else:
            print("\n❌ 未知命令! 可用命令: next, done <ID>, list, quit")


if __name__ == "__main__":
    main()