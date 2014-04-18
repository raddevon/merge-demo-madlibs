# -*- coding: utf-8 -*-


def get_data_interactive():
    words = []
    words.append(raw_input("Adjective: "))
    words.append(raw_input("Adjective: "))
    words.append(raw_input("Plural noun: "))
    words.append(raw_input("Adjective: "))
    words.append(raw_input("Adjective: "))
    words.append(raw_input("Adjective: "))
    words.append(raw_input("Verb ending in s: "))
    words.append(raw_input("Noun: "))
    words.append(raw_input("A kind of place: "))
    words.append(raw_input("Plural noun: "))
    words.append(raw_input("Adjective: "))
    words.append(raw_input("Plural noun: "))
    return words


def main():
    words = get_data_interactive()
    story = """Pia has grown up in a * laboratory hidden deep in the * rain forest. She was raised by a team of * who have created her to be the start of a new * race. But on the night of her seventeenth birthday, Pia discovers a hole in the * fence that surrounds her * home—and * outside the compound for the first time in her life.

Free in the jungle, Pia meets Eio, a * from a nearby *. Together, they embark on a race against * to discover the truth about Pia’s origin—a truth with * consequences that will change their * forever."""
    for current in range(0, story.count('*')):
        story = story.replace('*', words[current], 1)

    with open('story.txt', 'w') as f:
        f.write(story)

if __name__ == "__main__":
    main()
