import heapq

def merge_k_lists(lists):
    # Мінімальна купа
    min_heap = []
    
    # Ініціалізація купи з першими елементами кожного списку
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i][0], i, 0))
    
    merged_list = []
    step = 0
    
    while min_heap:
        # Вивід стану купи та результатного списку на поточному кроці
        print(f"Step {step}:")
        print(f"  Heap: {min_heap}")
        print(f"  Merged list: {merged_list}")
        
        # Витягуємо найменший елемент з купи
        val, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(val)
        
        # Вставляємо наступний елемент з цього списку в купу
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))
        
        step += 1
    
    # Остаточний стан
    print(f"Final step:")
    print(f"  Heap: {min_heap}")
    print(f"  Merged list: {merged_list}")
    
    return merged_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
