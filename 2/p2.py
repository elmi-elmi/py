# Unit test

def test_polygon():
   print('---------------------')
   
   try:
       print('Test 0')
       
       # 0
       n = 2
       r = 10
       p0 = Polygon(n, r)
       assert False, ("Creating a Polygon with 2 sides: "
                      " Exception expected, but not recieved")
   except ValueError:
       pass
   except:
       print("Test 0 passed")
   
   print('---------------------')
       
   print("Test 1 started")
   try:  
       
    # 1 
    n = 3 
    r = 10
    p1 = Polygon(3, 10)
    assert p1 == 'Polygon(vertices=3, radius=10)', "no repr"

   except:
       print("Test 1 failed")
   print('---------------------')

   print("Test 2 started")

test_polygon()
