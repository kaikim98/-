import tempfile

if __name__ == "__main__":
    with tempfile.TemporaryFile("w+") as tf:
        tf.write("사용자 정보")
        tf.seek(0)
        print(tf.read())
        print(tempfile.gettempdir())