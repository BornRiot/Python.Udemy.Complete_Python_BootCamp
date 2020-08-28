import one

print("TOP LEVEL IN TWO.PY")

# USE ONE.FUNC()
one.func1()

if __name__ == "__main__":
    print("TWO.PY IS BEING RAN DIRECTLY")
else:
    print('TWO.PY HAS BEEN IMPORTED')