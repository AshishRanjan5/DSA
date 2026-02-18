# Insertion Sort – Explanation with Sorted and Unsorted Portions

## Concept

Insertion Sort works the same way as arranging playing cards in your hand.
At any iteration:

* **Left portion (0 → i-1)** is **already sorted**
* **Current element (i)** is taken and inserted into the correct position inside the sorted portion
* **Right portion (i+1 → end)** remains **unsorted**

So during execution, the array is conceptually divided into:

```
[ Sorted Part | Unsorted Part ]
```

After every iteration, the sorted part grows by one element.

---

## Algorithm (Python Implementation)

```python
class InsertionSort:
  def sortArray(self, arr):
    for i in range(1, len(arr)):
      temp = arr[i]
      j = i - 1

      while j >= 0 and arr[j] > temp:
        arr[j + 1] = arr[j]
        j -= 1

      arr[j + 1] = temp

if __name__ == "__main__":
  insertionSort = InsertionSort()
  arr = [2, 4, 1, 3, 5]
  insertionSort.sortArray(arr)
  print(arr)
```

---

## Dry Run

Input array:

```
[2, 4, 1, 3, 5]
```

---

### Iteration 1 (i = 1)

```
Sorted   : [2]
Unsorted : [4, 1, 3, 5]
```

Insert **4** into sorted portion:

No shifting required.

```
Result : [2, 4, 1, 3, 5]
```

---

### Iteration 2 (i = 2)

```
Sorted   : [2, 4]
Unsorted : [1, 3, 5]
```

Insert **1**:

* 4 > 1 → shift
* 2 > 1 → shift

Place 1 at start.

```
Result : [1, 2, 4, 3, 5]
```

---

### Iteration 3 (i = 3)

```
Sorted   : [1, 2, 4]
Unsorted : [3, 5]
```

Insert **3**:

* 4 > 3 → shift
* 2 < 3 → stop

```
Result : [1, 2, 3, 4, 5]
```

---

### Iteration 4 (i = 4)

```
Sorted   : [1, 2, 3, 4]
Unsorted : [5]
```

Insert **5**:

No shifting needed.

```
Final Array : [1, 2, 3, 4, 5]
```

---

## Key Observations

* At each step, only **one element is inserted** into the sorted part.
* Best case (already sorted): **O(n)**
* Worst case (reverse sorted): **O(n²)**
* Stable sorting algorithm.
* Very efficient for **nearly sorted arrays**.
