import math
def analyze(levels, threshold):
    min_level = float('inf')
    max_level = float('-inf')
    total_q = 0.0
    n = len(levels)
    loud_count = 0
    first_loud = None
    last_loud = None
    current_fragment_start = None
    longest_fragment_start = None
    longest_fragment_end = None
    longest_length = 0
    best_fragment_q_sum = 0.0
    current_q_sum = 0.0
    current_length = 0
    for i, level in enumerate(levels):
        if level < min_level:
            min_level = level
        if level > max_level:
            max_level = level
        q = 10 ** (level / 10)
        total_q += q
        is_loud = level >= threshold
        if is_loud:
            loud_count += 1
            if first_loud is None:
                first_loud = i
            last_loud = i
            if current_fragment_start is None:
                current_fragment_start = i
                current_q_sum = q
                current_length = 1
            else:
                current_q_sum += q
                current_length += 1
        else:
            if current_fragment_start is not None:
                if current_length > longest_length:
                    longest_length = current_length
                    longest_fragment_start = current_fragment_start
                    longest_fragment_end = i - 1
                    best_fragment_q_sum = current_q_sum
                current_fragment_start = None
                current_q_sum = 0.0
                current_length = 0
    if current_fragment_start is not None and current_length > longest_length:
        longest_length = current_length
        longest_fragment_start = current_fragment_start
        longest_fragment_end = n - 1
        best_fragment_q_sum = current_q_sum
    eq_level_record = 10 * math.log10(total_q / n) if n > 0 else 0.0
    if longest_length > 0:
        eq_level_fragment = 10 * math.log10(best_fragment_q_sum / longest_length)
    else:
        eq_level_fragment = None
    return (
        min_level, max_level, eq_level_record,
        loud_count, first_loud, last_loud,
        longest_fragment_start, longest_fragment_end, eq_level_fragment
    )
def main():
    threshold = float(input().strip())
    levels_input = input().strip()
    if not levels_input:
        print("Нет записи")
        return
    levels = list(map(float, levels_input.split()))
    (
        min_level, max_level, eq_level_record,
        loud_count, first_loud, last_loud,
        frag_start, frag_end, eq_level_fragment
    ) = analyze(levels, threshold)
    print(f"Уровень: от {min_level:.1f} до {max_level:.1f} дБ")
    print(f"Эквивалентный уровень записи: {eq_level_record:.1f} дБ")
    print(f"Громких секунд: {loud_count}")
    if loud_count > 0:
        print(f"Первая громкая секунда: {first_loud}")
        print(f"Последняя громкая секунда: {last_loud}")
        print(f"Самый длинный фрагмент: {frag_start}-{frag_end}")
        print(f"Эквивалентный уровень фрагмента: {eq_level_fragment:.1f} дБ")
    else:
        print("Первая громкая секунда: нет")
        print("Последняя громкая секунда: нет")
        print("Самый длинный фрагмент: нет")
        print("Эквивалентный уровень фрагмента: нет")
if __name__ == "__main__":
    main()