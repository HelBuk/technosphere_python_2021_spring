# coding: utf8

class TicTacGame:
    table = list(range(1, 10))
    cnt = 0  # счетчик ходов
    r = 1    # показатель входа в цикл

    @staticmethod
    def show_board():
        print("_____________")
        for i in range(3):
            print("|", TicTacGame.table[3 * i], "|", TicTacGame.table[3 * i + 1], "|", TicTacGame.table[3 * i + 2], "|")
        print("_____________")

    @classmethod
    def validate_input(cls):
        n = input('Введите "Выход", если хотите закончить, или целое число от 1 до 9, чтобы продолжить игру:')
        if n == "Выход" or n == "выход":
            exit()
        else:
            try:
                n = int(n)
                if 1 <= n <= 9:
                    if (TicTacGame.table[n - 1] == 'x') | (TicTacGame.table[n - 1] == 'o'):
                        print('Это место занято')
                        return cls.validate_input()
                    else:
                        return n
                else:
                    print('Необходимо ввести "Выход", если хотите закончить, или целое число от 1 до 9')
                    return cls.validate_input()
            except:
                print('Необходимо ввести "Выход", если хотите закончить, или целое число от 1 до 9')
                return cls.validate_input()

    @classmethod
    def start_game(cls):
        cls.show_board()
        if TicTacGame.cnt % 2 == 0:
            print("Ход крестика")
            n = cls.validate_input()
            TicTacGame.table[n - 1] = 'x'

        else:
            print("Ход нолика")
            n = cls.validate_input()
            TicTacGame.table[n - 1] = 'o'
        cls.check_winner()


    @classmethod
    def check_winner(cls):
        res = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for each in res:
            if TicTacGame.table[each[0] - 1] == TicTacGame.table[each[1] - 1] == TicTacGame.table[each[2] - 1]:
                #print(TicTacGame.table[each[0] - 1] + " is winning ")
                return TicTacGame.table[each[0] - 1]
            elif TicTacGame.cnt == 8:
                print('Ничья')
                return 'Ничья'
        TicTacGame.cnt += 1
        print(TicTacGame.cnt)
        return cls.start_game()



if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
