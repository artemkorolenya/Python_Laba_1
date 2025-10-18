import time 


CSI = '\x1b['
RESET = f'{CSI}0m'

#УЗОР
def draw_line(left_offset, left_length, right_offset, right_length, color):
    total_length = max(left_offset + left_length, right_offset + right_length)
    line_chars = [' '] * total_length
    
    for i in range(left_offset, left_offset + left_length):
        if i < len(line_chars):
            line_chars[i] = f'{CSI}48;5;{color}m {RESET}'
    
    for i in range(right_offset, right_offset + right_length):
        if i < len(line_chars):
            line_chars[i] = f'{CSI}48;5;{color}m {RESET}'
    
    print(''.join(line_chars))


def draw_double_romb(height=16):
    center = height // 2
    step = 1
    
    left_offset = center
    left_length = 1
    right_offset = center * 3 
    right_length = 1
    
    connection_point = center
    
    color = 15
    
    for line in range(height):
        draw_line(left_offset, left_length, right_offset, right_length, color)        
        if line < connection_point:
            left_offset -= step 
            left_length += step * 2
            right_offset -= step
            right_length += step * 2
        elif line < center:
          
            left_offset -= step 
            left_length += step * 2
            right_offset -= step 
            right_length += step * 2
        else:
            left_offset += step
            left_length -= step * 2
            right_offset += step 
            right_length -= step * 2


if __name__ == '__main__':
    draw_double_romb()
#FLAG Бенина
def print_Benin_flag():
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    RED = '\033[41m'
    RESET = '\033[0m'
    height = 14
    green_width = 12
    main_width = 32
    
    for i in range(height):
        line = f"{GREEN}{' ' * green_width}{RESET}"
        if i < height // 2:
            line += f"{YELLOW}{' ' * main_width}{RESET}"
        else:
            line += f"{RED}{' ' * main_width}{RESET}"
        
        print(line)

print_Benin_flag()
#График y=x+1
height_graph=20
for i in range(1, height_graph):
    print(f'{CSI}48;5m{" "}{RESET}', end = "")
    for j in range(0, height_graph):
        if i == (height_graph- j-2):
            print(f'{CSI}48;5;15m  {RESET}', end = "")
        else:
            print(f'{CSI}48;5;16m  {RESET}', end = "")
    print()
time.sleep(1)
#Диаграмма
with open('sequence.txt', 'r') as f:
    nums = [float(line.strip()) for line in f if line.strip()]

    valid_nums = [n for n in nums if -5 <= n <= 5]
    pos = len([n for n in valid_nums if n >= 0])
    neg = len([n for n in valid_nums if n < 0])
    total = pos + neg  
    width = 40
    pos_bar = ' ' * int(pos/total * width)
    neg_bar = ' ' * int(neg/total * width)
    
    print(f" 0-5:    {CSI}48;5;9m{pos_bar}{RESET}{pos/total*100:.1f}%")

    print(f" 0-(-5): {CSI}48;5;122m{neg_bar}{RESET} {neg/total*100:.1f}%")

