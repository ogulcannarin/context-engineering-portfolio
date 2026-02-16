from tools.calculator import calculate
from tools.time_tool import get_time, get_datetime

# Tool registry
TOOLS = {
    "time": get_time,
    "datetime": get_datetime,
    "calculator": calculate,
}
