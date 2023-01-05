import datetime


class SystemInfo:
    def __int__(self):
        pass

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'São {} Horas e {} minutos.'.format(now.hour, now.minute)
        return answer
