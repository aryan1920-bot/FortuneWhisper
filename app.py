import streamlit as st
import random
import datetime
def roll_dice():
    num = random.randint(1, 6)
    return num

def get_fortune(num):
    fortunes = {
        1: "IT IS CERTAIN ",
        2: "DON'T COUNT ON IT ",
        3: "YES, DEFINITELY ",
        4: "SIGNS POINT TO YES ",
        5: "CANNOT PREDICT NOW ",
        6: "MY SOURCES SAY NO "
    }
    
    return fortunes.get(num)

def main():
    st.title('FORTUNE WHISPER :speak_no_evil:')
    st.text('SUMMON YOUR CURIOSITIES !!! ')
    current_year = datetime.datetime.now().year
    if st.button('ASK THE UNIVERSE :8ball:'):
        result = roll_dice()
        fortune = get_fortune(result)
        if fortune:
            st.text(fortune)
        emojis = [
            ':face_exhaling:', 
            ':no_mouth:', 
            ':raised_hands:', 
            ':grimacing:', 
            ':face_with_spiral_eyes:', 
            ':disappointed_relieved:'
        ]
        st.markdown(emojis[result - 1])                                     
    st.markdown('<div style="height: 250px;"></div>', unsafe_allow_html=True)
            
    st.markdown(
        f'<footer style="position: absolute; bottom: 0; width: 100%; text-align: center;">&copy; {current_year} Aryan Singla</footer>',
        unsafe_allow_html=True
    )
if __name__ == '__main__':
    main()


