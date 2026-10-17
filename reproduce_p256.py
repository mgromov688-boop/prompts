# Откуда взялось число АНБ для P-256: повтор расчёта из разбора Anthropic
# https://www.anthropic.com/research/ecdsa-curve-origins
# Генератор lrand48 из языка C, запущенный от времени на часах компьютера.
# Скрипт ничего не взламывает и никуда не подключается, только считает.
from datetime import datetime, timezone


def unix(when):
    return int(datetime.fromisoformat(when).replace(tzinfo=timezone.utc).timestamp())


def candidate(t, n, per, shift, width):
    x, out = (t << 16) | 0x330E, ""
    for i in range(per * n):
        x = (0x5DEECE66D * x + 0xB) % 2**48
        if i >= per * (n - 1):
            out += "%0*X" % (width, x >> shift)
    return out


seed = candidate(unix("1997-08-16 01:52:34"), 1842, per=20, shift=40, width=2)
print(seed)
print(seed == "C49D360886E704936A6678E1139D26B7819F7E90")
