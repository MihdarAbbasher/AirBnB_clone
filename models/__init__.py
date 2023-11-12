#!/usr/bin/python3
"""
Module: __init__ for initialization
"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
