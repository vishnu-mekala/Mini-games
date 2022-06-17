def main():
    print(exception())

def exception():
    try:
        return 1
        raise ZeroDivisionError('Hello')
    except Exception as error:
        print(error)
        return 2
    finally:
        return 4
main()