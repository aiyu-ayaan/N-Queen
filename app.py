import streamlit as st
from util.Utils import print_board_in_markdown, State
from engine.NQueen import NQueen

st.set_page_config(page_title='N-Queens Problem', page_icon=':chess_pawn:', layout='wide', initial_sidebar_state='auto')

main_container = st.container()
if State.N_QUEEN.value not in st.session_state:
    st.session_state[State.N_QUEEN] = NQueen()


def solve():
    with main_container:
        col1, col2 = st.columns(2)
        st.session_state[State.N_QUEEN].queen(board_size, col1, col2)


with main_container:
    board_size = st.slider('Select the number of queens', min_value=4, max_value=16, step=4)
    st.write(f'You selected {board_size} queens')
    st.markdown(print_board_in_markdown(board_size), unsafe_allow_html=True)
    st.button('Solve', on_click=solve)
