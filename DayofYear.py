class Solution:
    def dayOfYear(self, date: str) -> int:
        ano, mes, dia = map(int, date.split("-"))

        match mes:
            case 1:
                dia_do_ano = dia
            case 2:
                dia_do_ano = 31 + dia
            case 3:
                dia_do_ano = 59 + dia
            case 4:
                dia_do_ano = 90 + dia
            case 5:
                dia_do_ano = 120 + dia
            case 6:
                dia_do_ano = 151 + dia
            case 7:
                dia_do_ano = 181 + dia
            case 8:
                dia_do_ano = 212 + dia
            case 9:
                dia_do_ano = 243 + dia
            case 10:
                dia_do_ano = 273 + dia
            case 11:
                dia_do_ano = 304 + dia
            case 12:
                dia_do_ano = 334 + dia
        
        # Ajuste para anos bissextos
        if mes > 2 and ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)):
            dia_do_ano += 1

        return dia_do_ano

solution = Solution()
date = "2019-12-31"
print(solution.dayOfYear(date))
