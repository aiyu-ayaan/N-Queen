import time as t


class NQueen:
    def __init__(self):
        self.count = 0
        self.k = 1
        self.solutions = []  # List to store all solutions

    @staticmethod
    def place(arr, pos):
        for i in range(1, pos):
            if arr[i] == arr[pos] or abs(arr[i] - arr[pos]) == abs(i - pos):
                return False
        return True

    def print_sol(self, arr, n):
        solution = []
        for i in range(1, n + 1):
            line = ""
            for j in range(1, n + 1):
                if arr[i] == j:
                    line += "Q\t"
                else:
                    line += "*\t"
            solution.append(line)
        self.solutions.append(solution)

    @staticmethod
    def print_sol_in_markdown(solution):
        markdown = '```'
        markdown += '\n'
        for line in solution:
            markdown += line.replace("*", "#") + '\n'
        markdown += '```'
        return markdown

    def queen(self, n):
        start = t.time() * 1000
        arr = [0] * (n + 1)
        arr[self.k] = 0

        while self.k != 0:
            arr[self.k] += 1
            while arr[self.k] <= n and not self.place(arr, self.k):
                arr[self.k] += 1

            if arr[self.k] <= n:
                if self.k == n:
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
        return self.solutions, time  # Return solutions and time taken
        # if analysis_parent is not None:
        #     with analysis_parent:
        #         st.write(f'Total solutions: {self.count}')
        #         st.write(time)
        #
        # if board_parent:
        #     for i, solution in enumerate(self.solutions, start=1):
        #         if board_parent is not None:
        #             with board_parent:
        #                 with st.expander(f"Solution #{i}", expanded=True if i == 1 else False):
        #                     st.subheader(f"Solution #{i}:")
        #                     st.markdown(self.print_sol_in_markdown(self.solutions[-1]), unsafe_allow_html=True)
        # else:
        #     for i, solution in enumerate(self.solutions, start=1):
        #         print(f"Solution #{i}:")
        #         for line in solution:
        #             print(line)
        #         print()
        #     print(f'Total time taken : {time}')


if __name__ == '__main__':
    NQueen().queen(8)
