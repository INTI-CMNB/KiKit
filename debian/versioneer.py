import re

def get_version():
    with open("debian/changelog", "rt") as f:
        line = f.readline()
        m = re.match("kikit \(([\d\.]+\-\d+)\)", line)
        assert m
        version = m.group(1)
    with open("kikit/_version.py", "wt") as f:
        f.write("def get_versions():\n")
        f.write("    return {'version': '"+version+"'}\n")
    return version;
