import streamlit as st
import random

def roll_dice():
    num = random.randint(1, 6)
    return num

def get_fortune(num):
    fortunes = {
        1: "IT IS CERTAIN",
        2: "DON'T COUNT ON IT ",
        3: "YES, DEFINITELY",
        4: "SIGNS POINT TO YES",
        5: "CANNOT PREDICT NOW",
        6: "MY SOURCES SAY NO"
    }
    
    return fortunes.get(num)

def main():
    st.title('FORTUNE WHISPER')
    st.text('SPIN THE BALL:')
    if st.button(':8ball:'):
        result = roll_dice()
        fortune = get_fortune(result)
        if fortune:
            st.text(fortune)

if __name__ == '__main__':
    main()
