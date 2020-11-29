import os
from sys import argv

commit_bugfix = "🐛 FIX: "
commit_new = "📦 NEW: "
commit_doc = "📃 DOC: "
commit_release = "⛱ RELEASE: "
commit_improve = "🌱 IMPROVE: "

commands_commit = {
    "bugfix":commit_bugfix,
    "b":commit_bugfix,
    "bug":commit_bugfix,
    "fix":commit_bugfix,

    "new":commit_new,
    "n":commit_new,

    "doc":commit_doc,
    "d":commit_doc,

    "release":commit_release,
    "r":commit_release,

    "improve":commit_improve,
    "improvement":commit_improve,
    "imp":commit_improve,
    "i":commit_improve
}

def print_info():
    print("usage: cgit <command>")

def commit(arg):
    try:
        t = arg[2]
        if t in commands_commit:
            os.system('git commit -m "'+str(commands_commit[t]) + '" -e')
        
    except:
        os.system("git commit")

def main():
    try:
        command = argv[1]

        if command == "commit":
            commit(argv)








    except:
        print_info()

main()