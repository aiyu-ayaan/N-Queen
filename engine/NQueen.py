import time as t

import streamlit as st


class NQueen:
    def __init__(self):
        self.count = 0
        self.k = 1

    @staticmethod
    def place(arr, pos):
        for i in range(1, pos):
            if arr[i] == arr[pos] or abs(arr[i] - arr[pos]) == abs(i - pos):
                return False
        return True

    def print_sol(self, arr, n):
        print(f"\nSolution #{self.count}:")
        for i in range(1, n + 1):
            line = ""
            for j in range(1, n + 1):
                if arr[i] == j:
                    line += "Q\t"
                else:
                    line += "*\t"
            print(line)

    @staticmethod
    def print_sol_in_markdown(arr, n):
        markdown = '```'
        markdown += '\n'
        for i in range(1, n + 1):
            line = ""
            for j in range(1, n + 1):
                if arr[i] == j:
                    line += "Q\t"
                else:
                    line += "#\t"
            markdown += line + '\n'
        markdown += '```'
        return markdown

    def queen(self, n, board_parent: st.container = None, analysis_parent: st.container = None):
        start = t.time() * 1000
        arr = [0] * (n + 1)
        arr[self.k] = 0

        while self.k != 0:
            arr[self.k] += 1
            while arr[self.k] <= n and not self.place(arr, self.k):
                arr[self.k] += 1

            if arr[self.k] <= n:
                if self.k == n:
                    if board_parent is not None:
                        with board_parent:
                            with st.expander(f"Solution #{self.count + 1}",
                                             expanded=True if self.count == 0 else False):
                                st.subheader(f"Solution #{self.count + 1}:")
                                st.markdown(self.print_sol_in_markdown(arr, n), unsafe_allow_html=True)
                    else:
                        self.print_sol(arr, n)
                    self.count += 1
                else:
                    self.k += 1
                    arr[self.k] = 0
            else:
                self.k -= 1
        end = t.time() * 1000
        diff = end - start
        time = f'Time taken: {round(diff)} milliseconds' if diff < 1000 else f'Time taken: {round(diff / 1000)} seconds'
        if analysis_parent is not None:
            with analysis_parent:
                st.write(f'Total solution: {self.count}')
                st.write(time)


if __name__ == '__main__':
    NQueen().queen(12)
