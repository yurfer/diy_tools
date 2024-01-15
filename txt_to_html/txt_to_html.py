def convert_to_html(input_file, output_file):
    # 读取文本文件内容
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 生成 HTML 内容
    html_content = (
        "<html>\n"
        "<head>\n"
        "<style>\n"
        "  body { margin: 0; padding: 0; background: url(../高画質メインイラスト.png) no-repeat center center fixed; background-size: 100% auto; height: 100vh;  display: flex;  align-items: center; justify-content: center; font-family: 'Arial', sans-serif; background-color: #1a1a1a;}\n"
        "  div { text-align: center; font-size: 24px; color: #fff;  text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000; }\n"
        "</style>\n"
        "</head>\n"
        "<body>\n"
    )

    html_content += f" <div>\n"

    for line in lines:
        html_content += f"  <p>{line.strip()}</p>\n"

    html_content += f" </div>\n"

    html_content += (
        "</body>\n"
        "</html>"
    )

    # 将 HTML 内容写入文件
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    print(f"生成的 HTML 已保存到 {output_file}")


if __name__ == "__main__":
    input_path = "input.txt"  # 输入的文本文件路径
    output_path = "output.html"  # 输出的 HTML 文件路径

    convert_to_html(input_path, output_path)
