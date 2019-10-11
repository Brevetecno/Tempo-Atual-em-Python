from datetime import datetime
from time import sleep

class StartTime():
    def __init__(self):
        
        # Pega tempo atual: data, ano, mês, dia, horas, minutos, segundos
        class DateTimeNow():
            def year_now(self): # Retornar o ano atual
                self.dt = datetime.now()
                self.year = self.dt.year
                return self.year
            def month_now(self): # Retorna o mês atual
                self.dt = datetime.now()
                self.month = self.dt.month
                return self.month
            def day_now(self): # Retorna o dia atual
                self.dt = datetime.now()
                self.day = self.dt.day
                return self.day
            def hour_now(self): # Retorna a hora atual
                self.dt = datetime.now()
                self.hour = self.dt.hour
                return self.hour
            def minute_now(self): # Retorna o minuto atual
                self.dt = datetime.now()
                self.minute = self.dt.minute
                return self.minute
            def second_now(self): # Retorna os segundos atuais
                self.dt = datetime.now()
                self.second = self.dt.second
                return self.second
            def date_now(self): # Retorna a data atual
                self_d = self.day_now()   # Pega dia atual
                self_m = self.month_now()   # Pega mês atual
                self_y = self.year_now()     # Pega ano atual
                self.date = ('{}/{}/{}'.format(self_d, self_m, self_y)) # xx/yy/zz
                return self.date
            def time_now(self): # Retorna a hora atual
                self.h = self.hour_now()
                self.m = self.minute_now()
                self.s = self.second_now()

                if self.h < 10:
                    self.h = '0' + str(self.h)
                if self.m < 10:
                    self.m = '0' + str(self.m)
                if self.s < 10:
                    self.s = '0' + str(self.s)

                self.time = ('{}:{}:{}'.format(self.h, self.m, self.s))
                return self.time
        while True: # Atualiza a hora no console
            print('-'*50)
            print('Horário: ', DateTimeNow().time_now())
            print('Data', DateTimeNow().date_now())
            sleep(1)

#Iniciar
StartTime()

