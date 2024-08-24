import os

blocks = ["users", "pet", "store"]
#blocks = ["users"]
cmd = " ".join(f"tests/{block}.py" for block in blocks)

os.system(f"pytest {cmd} --maxfail=1")