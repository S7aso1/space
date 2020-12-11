
def get_lines():
    print('Write me some text: ')
    text_collector = []
    counter = 0

    while True: 
        text_input = input()

        if text_input == '':
            counter += 1
        else:
            counter = 0
        
        text_collector.append(text_input)

        if counter == 2:
            break
    
    return('\n'.join(text_collector))


def analyze_text(text):
    words = text.split()

    print(words) 
    longestWordLen = max([len(word) for word in words])
    count_words = len(words)

    return longestWordLen, count_words

print(analyze_text(get_lines()))
