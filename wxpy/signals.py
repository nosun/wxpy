from blinker import Namespace

_signals = Namespace()

stopped = _signals.signal('stopped')
