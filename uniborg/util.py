from telethon import events
from sample_config import Config
from cyborg.ubutil import admin_cmd as ac
from cyborg.ubutil import is_read as ir
from cyborg.ubutil import progress as pg
from cyborg.ubutil import humanbytes as hb
from cyborg.ubutil import time_formatter as tf

def admin_cmd(pattern=None, allow_sudo=True, outgoing=True, incoming=False, allow_edited_updates=False):
    return ac(pattern)

async def is_read(borg, entity, message, is_out=None):
    ir(borg, entity, message, is_out)

def progress(current, total, event, start, type_of_ps):
    return pg(current, total, event, start, type_of_ps)

def humanbytes(size):
    return hb(size)

def time_formatter(milliseconds: int) -> str:
    return tf(milliseconds)
