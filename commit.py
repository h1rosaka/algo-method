import subprocess

# gitコマンドを実行する関数
def git(command):
    return subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

# git statusを実行し、新規追加されたファイルの一覧を取得する
status_output = git("git status --porcelain")
added_files = [line.split()[1] for line in status_output.stdout.splitlines() if line.startswith("??")]

# 新規追加されたファイルを1ファイルずつステージングしてコミットする
for file in added_files:
    git(f"git add {file}")
    commit_message = "good job"
    git(f"git commit -m '{commit_message}' {file}")
