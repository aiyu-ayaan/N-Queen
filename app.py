import threading
import time as t

import streamlit as st
from streamlit.runtime.scriptrunner import add_script_run_ctx

from engine.NQueen import NQueen
from util.Utils import print_board_in_markdown, State

st.set_page_config(page_title='N-Queens Problem', page_icon=':chess_pawn:', layout='wide', initial_sidebar_state='auto')

main_container = st.container()

if State.N_QUEEN.value not in st.session_state:
    st.session_state[State.N_QUEEN] = NQueen()


@st.cache_data()
def solve_n_queens(n):
    print(f"Running N-Queens for {n} queens")
    solutions, count = NQueen().queen(n)
    return solutions, count


def run_solver(n, board_parent, analysis_parent):
    thread = threading.Thread(target=solve_and_display, args=(n, board_parent, analysis_parent))
    add_script_run_ctx(thread)
    thread.start()
    thread.join()


def solve_and_display(n, board_parent, analysis_parent):
    start = t.time() * 1000
    solutions, count = solve_n_queens(n)
    print(f"Total solutions: {count} , Time taken: {t.time() * 1000 - start} milliseconds")
    end = t.time() * 1000
    diff = end - start
    time_str = f'Time taken: {round(diff)} milliseconds' if diff < 1000 else f'Time taken: {round(diff / 1000)} seconds'

    if analysis_parent is not None:
        with analysis_parent:
            st.write(f'Total solutions: {(len(solutions))}')
            st.write(time_str)

    if board_parent:
        if len(solutions) == 0:
            with board_parent:
                st.write("No solutions found")
            return
        if len(solutions) <= 100:
            for i, solution in enumerate(solutions, start=1):
                if board_parent is not None:
                    with board_parent:
                        with st.expander(f"Solution #{i}", expanded=True if i == 1 else False):
                            st.subheader(f"Solution #{i}:")
                            st.markdown(NQueen.print_sol_in_markdown(solution), unsafe_allow_html=True)
        else:
            st.write(f"Total solutions: {len(solutions)}")
            for i, solution in enumerate(solutions[:100], start=1):
                if board_parent is not None:
                    with board_parent:
                        with st.expander(f"Solution #{i}", expanded=True if i == 1 else False):
                            st.subheader(f"Solution #{i}:")
                            st.markdown(NQueen.print_sol_in_markdown(solution), unsafe_allow_html=True)


board_container, analysis_container = st.columns(2)
with main_container:
    board_size = st.slider('Select the number of queens', min_value=4, max_value=16, step=4)
    st.write(f'You selected {board_size} queens')
    st.markdown(print_board_in_markdown(board_size), unsafe_allow_html=True)
    if st.button("Solve"):
        run_solver(board_size, board_container, analysis_container)
