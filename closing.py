
class Closing:
    
    def closing(self):
        finally:
            try:
                sc.close()
            except:
                print("Context didn't get closed")
