class employee:
    def __init__(self):
        print("emloyee creted")

    def __del__(self):
        print("employee deleted")

ob = employee()
del ob