
def test_cryptography():
    try:
        print("Cryptography library is installed and working.")
    except ImportError:
        print("Cryptography library is not installed.")

test_cryptography()