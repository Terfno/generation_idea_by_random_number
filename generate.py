import sys
import random

action_path = ("./action.txt")
app_path = ("./app.txt")
goal_path = ("./goal.txt")
viewpoint_path = ("./viewpoint.txt")


def getArray(file_name):
    try:
        file = open(file_name)
        result = []
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            result.append(line)
    except Exception as e:
        print(e)
    finally:
        file.close()
        return result

def main():
    goal = getArray(goal_path)
    viewpoint = getArray(viewpoint_path)
    action = getArray(action_path)
    app = getArray(app_path)

    print("パターン数："+str(len(goal))+"×"+str(len(viewpoint))+"×"+str(len(action))+"×"+str(len(app))+"="+str(len(goal)*len(viewpoint)*len(action)*len(app))+"パターン")

    print(goal[random.randrange(len(goal))] + viewpoint[random.randrange(len(viewpoint))] + action[random.randrange(len(action))] + app[random.randrange(len(app))] + "を作る")

main()
