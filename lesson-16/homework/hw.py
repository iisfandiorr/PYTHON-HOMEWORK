

### **1. Convert List to 1D Array**

```python
import numpy as np

my_list = [12.23, 13.32, 100, 36.32]
my_arr = np.array(my_list)
print(my_arr)
```

-----

### **2. Create 3x3 Matrix (2?10)**

```python
import numpy as np
test = np.array([[2,3,4],[5,6,7],[8,9,10]])
print(test)
```

-----

### **3. Null Vector (10) & Update Sixth Value**

```python
import numpy as np
test = np.zeros(10)
test[6] = 11
print(test)
```

-----

### **4. Array from 12 to 38**

```python
import numpy as np

array = np.arange(12, 38)

print(array)
```

-----

### **5. Convert Array to Float Type**

```python
import numpy as np

arr1 = np.array([1,2,3,4])
print(arr1)
arr1.dtype = 'float64'
arr1.dtype
```

-----

### **6. Celsius to Fahrenheit Conversion**

```python
import numpy as np

C = np.array([0, 12, 45.21, 34, 99.91])

F = C * 9/5 + 32
C_back = (F - 32) * 5/9

print("Values in Fahrenheit degrees:")
print(F)

print("\nValues in Centigrade degrees:")
print(C_back)
```

-----

### **7. Append Values to Array (Do self-tudy)**

```python
import numpy as np

arr = np.array([10, 20, 30])
print("Original array:")
print(arr)

new_arr = np.append(arr, [40, 50, 60, 70, 80, 90])
print("After append values to the end of the array:")
print(new_arr)
```

-----

### **8. Array Statistical Functions (Do self-tudy)**

```python
import numpy as np
arr = np.random.rand(10)
mean_val = np.mean(arr)
median_val = np.median(arr)
std_val = np.std(arr)
print("Array:", arr)
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard deviation:", std_val)
```

-----

### **9 Find min and max**

```python
import numpy as np
arr = np.random.rand(10, 10)
print(arr)
print('The minimum is:')
print(np.min(arr))
print('The maximum is:')
print(np.max(arr))
```

-----

### **10**

```python
import numpy as np

array = np.random.randn(3, 3, 3)

print(array)
