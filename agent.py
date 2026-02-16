from api_handler import get_weather

def process_query(query):
    query_lower = query.lower()

    # Check if user wants weather
    if "weather" in query_lower:
        # Extract city name if user typed "weather in CITY"
        if "in" in query_lower:
            city = query_lower.split("in")[-1].strip()
        else:
            city = "Hyderabad"  # default city
        return get_weather(city)

    elif "report" in query_lower:
        return "Generating report..."

    elif "error" in query_lower:
        return "Analyzing error..."

    else:
        return "AI is thinking..."



