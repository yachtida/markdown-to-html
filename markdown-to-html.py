import markdown
import sys


def main():
    if len(sys.argv) < 2:
        print("使用方法: python markdown-to-html.py <Markdownファイル>")
        sys.exit(1)
    md_file = sys.argv[1]
    md_content = read_markdown_file(md_file)
    html_content = convert_md_to_html(md_content)

    if html_content:
        output_file = md_file.rsplit('.', 1)[0] + '.html'
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"HTMLファイルが正常に生成されました: {output_file}")
        except IOError:
            print(f"エラー: HTMLファイル '{output_file}' を書き込めません。")
            sys.exit(1)
    else:
        print("Markdownの変換に失敗しました。")
        sys.exit(1)

if __name__ == "__main__":
    main()



def read_markdown_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"エラー: ファイル '{file_path}' が見つかりません。")
        sys.exit(1)
    except IOError:
        print(f"エラー: ファイル '{file_path}' を読み込めません。")
        sys.exit(1)


def convert_md_to_html(md_content):
    try:
        html_content = markdown.markdown(md_content)
        return html_content
    except Exception as e:
        print(f"エラー: Markdownの変換中に問題が発生しました。{str(e)}")
        return None


if __name__ == "__main__":
    main()