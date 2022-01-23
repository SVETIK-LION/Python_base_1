def convert_time(duration: int) -> str:
    days = duration // 86400
    hours = (duration - days * 86400) // 3600
    minutes = (duration - days * 86400 - hours * 3600) // 60
    seconds = duration - days * 86400 - hours * 3600 - minutes * 60
    if days > 0:
        res = f'{days} дн {hours} час {minutes} мин {seconds} сек'
    elif hours > 0:
        res = f'{hours} час {minutes} мин {seconds} сек'
    elif minutes > 0:
        res = f'{minutes} мин {seconds} сек'
    elif seconds > 0:
        res = f'{seconds} сек'
    return res


duration = 400003
result = convert_time(duration)
print(result)