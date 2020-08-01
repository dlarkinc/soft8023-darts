from dao import darts_match_dao
from domain import darts_match

dao = darts_match_dao.DartsMatchDao()

match = darts_match.DartsMatch('501', 'Dupe', 'Dup1')

dao.add(match)