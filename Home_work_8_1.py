import heapq
import matplotlib.pyplot as plt

def min_cost_to_connect_cables_graph(cables):
    # Перетворюємо список кабелів у мінімальну купу
    heapq.heapify(cables)
    
    total_cost = 0
    steps = []
    
    while len(cables) > 1:
        # Витягуємо два найкоротших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Об'єднуємо їх
        cost = first + second
        total_cost += cost
        
        # Зберігаємо крок для графіка
        steps.append((first, second, cost))
        
        # Вставляємо новий кабель назад у купу
        heapq.heappush(cables, cost)
    
    # Відображаємо графік
    fig, ax = plt.subplots()
    ax.set_title("Процес об'єднання кабелів")
    ax.set_xlabel("Номер кроку")
    ax.set_ylabel("Довжина кабелів")
    
    # Ініціалізуємо лінії для кожного кроку
    for i, (first, second, cost) in enumerate(steps):
        ax.plot([i * 2, i * 2], [0, first], 'r', label='Перший кабель' if i == 0 else "")
        ax.plot([i * 2 + 1, i * 2 + 1], [0, second], 'b', label='Другий кабель' if i == 0 else "")
        ax.plot([i * 2 + 2, i * 2 + 2], [0, cost], 'g', label='Об\'єднаний кабель' if i == 0 else "")
    
    # Відображаємо легенду 
    handles, labels = ax.get_legend_handles_labels()
    unique_labels = dict(zip(labels, handles))
    ax.legend(unique_labels.values(), unique_labels.keys())
    
    plt.show()
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables_graph(cables))
