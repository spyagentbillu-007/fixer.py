import ast
import os

# COLORS
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

def banner():
    os.system("clear")
    print(f"""{R}
███╗   ███╗██████╗     ██████╗ ██╗██╗      █████╗ ██╗     
████╗ ████║██╔══██╗    ██╔══██╗██║██║     ██╔══██╗██║     
██╔████╔██║██████╔╝    ██████╔╝██║██║     ███████║██║     
██║╚██╔╝██║██╔══██╗    ██╔══██╗██║██║     ██╔══██║██║     
██║ ╚═╝ ██║██║  ██║    ██████╔╝██║███████╗██║  ██║███████╗
╚═╝     ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
{C}====================================================
{Y}   🔥 MR.BILAL AUTO FIXER TOOL 🔥
{G}   Author : Mr.Bilal
{C}===================================================={W}
""")

def fix_code(code):
    lines = code.split("\n")
    fixed = []

    for line in lines:
        # tabs → spaces
        line = line.replace("\t", "    ")

        # fix missing colon (basic)
        if line.strip().startswith(("if ","for ","while ","def ","class ")) and not line.strip().endswith(":"):
            line += ":"

        fixed.append(line)

    return "\n".join(fixed)

def check_and_fix(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()

        # try parsing
        ast.parse(code)
        print(G + "✅ No Syntax Error Found")
        return

    except SyntaxError as e:
        print(R + f"❌ Error at line {e.lineno}: {e.msg}")
        print(Y + "⚡ Trying Auto Fix...")

        fixed_code = fix_code(code)

        new_file = "fixed_" + os.path.basename(file_path)
        with open(new_file, "w", encoding="utf-8") as f:
            f.write(fixed_code)

        print(G + f"✅ Fixed file saved as: {new_file}")

def main():
    banner()
    file_path = input(W + "Enter script path: ")

    if not os.path.exists(file_path):
        print(R + "❌ File not found")
        return

    check_and_fix(file_path)

if __name__ == "__main__":
    main()