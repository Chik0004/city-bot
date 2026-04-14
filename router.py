from scraper import get_city_news

BASE_URL = "https://www.normanok.gov"

def generate_response(user_input):
    user_input = user_input.lower()

    # 👋 Greeting
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return [
            "Hey! 😊 I'm your City Assistant 🏙️\n\nHow can I help you today?\n\n"
            "You can ask about:\n"
            "• Pay bills\n"
            "• Potholes / complaints\n"
            "• Public safety\n"
            "• Jobs\n"
            "• News & events"
        ]

    # 💳 Pay Online
    elif "pay" in user_input or "bill" in user_input:
        return [
            "💳 You can pay your bills here:\n\n"
            f"{BASE_URL}/online-payments"
        ]

    # 🚧 Potholes / complaints
    elif "pothole" in user_input or "complaint" in user_input or "report" in user_input:
        return [
            "🚧 You can report issues like potholes here:\n\n"
            f"{BASE_URL}/ActionCenter"
        ]

    # 🚓 Public Safety
    elif "police" in user_input or "safety" in user_input:
        return [
            "🚓 Public Safety Information:\n\n"
            f"{BASE_URL}/public-safety\n\n"
            "📞 Non-Emergency Police: 405-321-1444"
        ]

    # 🧑‍💼 Jobs
    elif "job" in user_input or "career" in user_input:
        return [
            "🧑‍💼 Explore job opportunities here:\n\n"
            f"{BASE_URL}/Careers"
        ]

    # 📰 News (Scraper still used!)
    elif "news" in user_input or "latest" in user_input:
        news = get_city_news()

        formatted_news = []
        for item in news:
            formatted_news.append(f"**{item['title']}**\n🔗 {item['link']}")

        return ["📰 Latest City News:\n\n" + "\n\n".join(formatted_news)]

    # 🎉 Events
    elif "event" in user_input:
        return [
            "🎉 Check out upcoming events:\n\n"
            f"{BASE_URL}/events"
        ]

    # 🏢 Departments
    elif "department" in user_input:
        return [
            "🏢 Find a department here:\n\n"
            f"{BASE_URL}/departments"
        ]

    # ❓ Default
    else:
        return [
            "Hmm 🤔 I didn’t understand that.\n\nTry asking:\n"
            "• pay bill\n"
            "• pothole report\n"
            "• jobs\n"
            "• latest news\n"
            "• events"
        ]
