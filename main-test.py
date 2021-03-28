from main import Add

def TestAdd():
        assert Add(2,3) == 5
		assert Add(2,4) == 7
        print("Add Function works correctly")

if __name__ == '__main__':
        TestAdd()