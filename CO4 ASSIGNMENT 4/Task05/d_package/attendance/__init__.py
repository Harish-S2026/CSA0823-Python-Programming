"""Attendance processing package."""
from .reader import read_records
from .stats import percentage, absent_three_days
from .report import write_report
