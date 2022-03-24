import os
import io
from logging import StreamHandler
from logging.handlers import MemoryHandler, TimedRotatingFileHandler

FORCE_FLUSH_TAG = "__flush__"

class MyMemoryHandler(MemoryHandler):

    def emit(self, record):
        if self.capacity <= len(self.buffer):
            del self.buffer[0]
        super().emit(record)

    def shouldFlush(self, record):
        if record.msg == FORCE_FLUSH_TAG:
            return True
        return (record.levelno >= self.flushLevel)

    def flush(self):
        # memo: logging.shutdown()からはshouldFlush()を経由せずに呼ばれるので再チェックがいる
        if self.buffer and self.shouldFlush(self.buffer[-1]):
            super().flush()
            


class StringHandler(StreamHandler):
    """ログ出力を変数に格納する独自Handler"""
    str_io = io.StringIO()
    def __init__(self):
        # self.str_io = io.StringIO()
        StreamHandler.__init__(self, StringHandler.str_io)
        
    @staticmethod
    def flush():
        buf = StringHandler.str_io.getvalue()
        #StringHandler.str_io.
        #StringHandler.str_io.close()
        return buf
    
    
class MyFileRotationHandler(TimedRotatingFileHandler):
    
    def __init__(self, *args, **kwargs):
        os.makedirs(os.path.dirname(kwargs["filename"]), exist_ok=True)
        super().__init__(*args, **kwargs)
        