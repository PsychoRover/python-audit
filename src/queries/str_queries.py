DISTINCT_COMMANDS = """SELECT name
FROM sqlite_master
WHERE type = 'table'
ORDER BY name
"""
