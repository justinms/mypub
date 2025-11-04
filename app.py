import argparse

def add_ok(s: str) -> str:
    """
    一个简单的处理函数，在输入字符串后面加上 ", ok!"
    你可以将这里的逻辑替换为任何你想要的复杂处理，比如调用 API、分析文本等。
    """
    return f"{s}, ok!"

if __name__ == "__main__":
    # 1. 设置命令行参数解析器
    parser = argparse.ArgumentParser(description="Process issue data and generate a response.")
    parser.add_argument("--title", required=True, help="The title of the GitHub issue.")
    parser.add_argument("--message", required=True, help="The content of the comment that triggered the action.")
    
    # 2. 解析传入的参数
    args = parser.parse_args()
    
    # 3. 构建输入字符串
    # 为了演示，我们将标题和消息组合起来
    input_string = f"Bot received mention regarding issue '{args.title}'. The triggering message was: '{args.message}'"
    
    # 4. 调用处理函数生成回复
    response = add_ok(input_string)
    
    # 5. 将最终结果打印到标准输出
    # GitHub Actions 将会捕获这个输出
    print(response)