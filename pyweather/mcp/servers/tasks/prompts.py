from pyweather.mcp.servers.tasks.server import mcp


@mcp.prompt()
def plan_trip_prompt(destination: str, duration_in_days: int) -> str:
    """
    Creates a sample travel itinerary for a given destination and duration, then saves it as a series of tasks in the user's to-do list.
    This is the best prompt to use when a user asks to plan a trip, create an itinerary, or asks for travel suggestions.

    Args:
        destination: The city or country for the trip (e.g., "Paris", "Japan").
        duration_in_days: The number of days for the trip (e.g., 3).
    """
    return f"""
    You are an expert travel consultant. Your goal is to help the user by generating a sample travel itinerary and saving it to their task list for later reference.

    The user wants a plan for a {duration_in_days}-day trip to {destination}.

    Follow these steps carefully:
    1.  First, use your general knowledge to brainstorm a simple, day-by-day itinerary. Suggest one or two key attractions or activities for each day of the trip.
    2.  After you have formulated the plan, you MUST perform a critical action: for each individual activity or attraction in your suggested itinerary, save it to the user's task list. For example, if you suggest visiting the Louvre, you must call the tool for that specific item.
    3.  Once all the itinerary items have been added as tasks, present a friendly confirmation message to the user. Inform them that you have created a sample plan and saved it to their to-do list.
    """