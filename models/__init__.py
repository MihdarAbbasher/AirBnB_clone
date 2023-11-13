#!/usr/bin/python3
"""
Module: __init__ for initialization
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
